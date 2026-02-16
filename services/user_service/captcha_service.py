import base64
import secrets
from fastapi import HTTPException, status
from captcha.image import ImageCaptcha
from cachetools import TTLCache
from core.constants import CAPTCHA_CACHE, captcha_cache


class CaptchaService:
    @staticmethod
    async def generate_captcha():
        image = ImageCaptcha()
        captcha_text = secrets.token_hex(3)
        captcha_id = secrets.token_urlsafe(8)
        image.character_rotate = (-40, 40)
        image.character_offset_dy = (0, 6)
        data = image.generate(captcha_text)
        image_bytes = data.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        captcha_cache[captcha_id] = captcha_text
        print(captcha_text)
        return captcha_id, image_base64

    @staticmethod
    async def verify_captcha(captcha_id: str, captcha_answer: str):
        stored_captcha = captcha_cache.get(captcha_id)

        if not stored_captcha:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Captcha expired or invalid"
            )

        if stored_captcha.lower() != captcha_answer.lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid captcha answer"
            )

        del captcha_cache[captcha_id]


captcha_service = CaptchaService()
