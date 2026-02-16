import base64
import secrets
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from utils.security import hash_password
from models.auth_model import User
from captcha.image import ImageCaptcha
from cachetools import TTLCache

CAPTCHA_CACHE = TTLCache(maxsize=1000, ttl=300)
captcha_cache = CAPTCHA_CACHE


async def create_user(db: AsyncSession, *, email: str, first_name: str,
                      last_name: str, password: str) -> User:
    res = await db.execute(select(User).where(User.email == email))
    if res.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=hash_password(password),
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


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
