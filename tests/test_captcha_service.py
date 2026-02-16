import pytest
import base64
from unittest.mock import patch, MagicMock
from fastapi import HTTPException, status
from services.user_service.captcha_service import CaptchaService, captcha_service
from core.constants import captcha_cache


@pytest.fixture
def clean_captcha_cache():
    captcha_cache.clear()
    yield
    captcha_cache.clear()


@pytest.fixture
def captcha_service_instance():
    return CaptchaService()


class TestCaptchaService:

    @pytest.mark.asyncio
    async def test_generate_captcha_returns_id_and_image(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id, image_base64 = await captcha_service_instance.generate_captcha()

        assert captcha_id is not None
        assert len(captcha_id) > 0
        assert image_base64 is not None
        assert len(image_base64) > 0
        try:
            base64.b64decode(image_base64)
        except Exception:
            pytest.fail("image_base64 is not valid base64 string")
        assert captcha_id in captcha_cache


    @pytest.mark.asyncio
    async def test_generate_captcha_stores_in_cache(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id, _ = await captcha_service_instance.generate_captcha()
        stored_value = captcha_cache.get(captcha_id)
        assert stored_value is not None
        assert len(stored_value) == 6


    @pytest.mark.asyncio
    async def test_generate_captcha_unique_ids(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id_1, _ = await captcha_service_instance.generate_captcha()
        captcha_id_2, _ = await captcha_service_instance.generate_captcha()

        assert captcha_id_1 != captcha_id_2
        assert captcha_id_1 in captcha_cache
        assert captcha_id_2 in captcha_cache


    @pytest.mark.asyncio
    async def test_verify_captcha_success(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id, _ = await captcha_service_instance.generate_captcha()
        correct_answer = captcha_cache[captcha_id]
        await captcha_service_instance.verify_captcha(captcha_id, correct_answer)
        assert captcha_id not in captcha_cache


    @pytest.mark.asyncio
    async def test_verify_captcha_case_insensitive(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id, _ = await captcha_service_instance.generate_captcha()
        correct_answer = captcha_cache[captcha_id]
        await captcha_service_instance.verify_captcha(
            captcha_id, correct_answer.upper()
        )
        assert captcha_id not in captcha_cache


    @pytest.mark.asyncio
    async def test_verify_captcha_invalid_answer(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id, _ = await captcha_service_instance.generate_captcha()
        wrong_answer = "wronganswer123"

        with pytest.raises(HTTPException) as exc_info:
            await captcha_service_instance.verify_captcha(captcha_id, wrong_answer)

        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert exc_info.value.detail == "Invalid captcha answer"
        assert captcha_id in captcha_cache


    @pytest.mark.asyncio
    async def test_verify_captcha_expired_or_invalid_id(
        self, captcha_service_instance, clean_captcha_cache
    ):
        non_existent_id = "nonexistent_captcha_id"
        with pytest.raises(HTTPException) as exc_info:
            await captcha_service_instance.verify_captcha(
                non_existent_id, "someanswer"
            )

        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert exc_info.value.detail == "Captcha expired or invalid"


    @pytest.mark.asyncio
    async def test_verify_captcha_removes_from_cache_after_success(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id, _ = await captcha_service_instance.generate_captcha()
        correct_answer = captcha_cache[captcha_id]
        assert captcha_id in captcha_cache
        await captcha_service_instance.verify_captcha(captcha_id, correct_answer)
        assert captcha_id not in captcha_cache
        with pytest.raises(HTTPException) as exc_info:
            await captcha_service_instance.verify_captcha(captcha_id, correct_answer)

        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert exc_info.value.detail == "Captcha expired or invalid"


    @pytest.mark.asyncio
    async def test_verify_captcha_empty_answer(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id, _ = await captcha_service_instance.generate_captcha()
        with pytest.raises(HTTPException) as exc_info:
            await captcha_service_instance.verify_captcha(captcha_id, "")

        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert exc_info.value.detail == "Invalid captcha answer"


    @pytest.mark.asyncio
    async def test_captcha_service_singleton(self):
        from services.user_service.captcha_service import captcha_service as imported_service

        assert isinstance(imported_service, CaptchaService)


    @pytest.mark.asyncio
    async def test_multiple_captcha_generation(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captchas = []
        for _ in range(5):
            captcha_id, image_base64 = await captcha_service_instance.generate_captcha()
            captchas.append((captcha_id, image_base64))

        captcha_ids = [c[0] for c in captchas]
        assert len(captcha_ids) == len(set(captcha_ids))

        images = [c[1] for c in captchas]
        assert len(set(images)) == 5
        for captcha_id, _ in captchas:
            assert captcha_id in captcha_cache


    @pytest.mark.asyncio
    async def test_verify_multiple_captchas_independently(
        self, captcha_service_instance, clean_captcha_cache
    ):
        captcha_id_1, _ = await captcha_service_instance.generate_captcha()
        captcha_id_2, _ = await captcha_service_instance.generate_captcha()

        answer_1 = captcha_cache[captcha_id_1]
        answer_2 = captcha_cache[captcha_id_2]
        await captcha_service_instance.verify_captcha(captcha_id_1, answer_1)
        assert captcha_id_1 not in captcha_cache
        assert captcha_id_2 in captcha_cache
        await captcha_service_instance.verify_captcha(captcha_id_2, answer_2)
        assert captcha_id_1 not in captcha_cache
        assert captcha_id_2 not in captcha_cache
