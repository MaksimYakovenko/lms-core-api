from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.auth import SignUpRequest, SignUpResponse
from services.auth_service import create_user

router = APIRouter(prefix="/auth", tags=["Auth"])


# @router.post("/sign-in", response_model=TokenOut)
# async def sign_in(payload: SignUpIn, db: AsyncSession = Depends(get_db)):
#     res = await db.execute(select(User).where(User.email == payload.email))
#     user = res.scalar_one_or_none()
#
#     if not user or not verify_password(payload.password, user.password_hash):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid credentials"
#         )
#
#     token = create_access_token({"sub": str(user.id), "email": user.email})
#     return {"access_token": token, "token_type": "bearer"}


@router.post("/sign-up", status_code=status.HTTP_201_CREATED, response_model=SignUpResponse)
async def sign_up(payload: SignUpRequest, db: AsyncSession = Depends(get_db)):
    await create_user(
        db,
        email=payload.email,
        first_name=payload.first_name,
        last_name=payload.last_name,
        password=payload.password,
    )
    return {"message": "User created"}


