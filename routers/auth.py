from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.auth import SignUpRequest, SignUpResponse, SignInRequest, \
    SignInResponse
from services.user_service.sign_up_service import auth_service
from services.user_service.sign_in_service import sign_in_service
from services.user_service.captcha_service import captcha_cache, captcha_service
from utils.jwt import create_access_token
from utils.dependencies import get_current_user
from models.auth_model import User

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/sign-in", response_model=SignInResponse)
async def sign_in(payload: SignInRequest, db: AsyncSession = Depends(get_db)):
    token = await sign_in_service.sign_in(
        db,
        email=payload.email,
        password=payload.password
    )
    return SignInResponse(access_token=token)


@router.post("/sign-up", response_model=SignUpResponse)
async def sign_up(payload: SignUpRequest, db: AsyncSession = Depends(get_db)):
    await auth_service.create_user(
        db,
        email=payload.email,
        first_name=payload.first_name,
        last_name=payload.last_name,
        password=payload.password,
        birthday=payload.birthday,
        captcha_id=payload.captcha_id,
        captcha_answer=payload.captcha_answer,
    )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "User created"}
    )


@router.get("/captcha")
async def get_captcha():
    captcha_id, image_base64 = await captcha_service.generate_captcha()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"captcha_id": captcha_id, "image": image_base64}
    )
