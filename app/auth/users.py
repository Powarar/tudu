from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.settings import get_auth_data

from app.repositories.users import get_user_by_username


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    print(f"DEBUG: Password length is {len(password)}")
    print(f"DEBUG: Password bytes length is {len(password.encode('utf-8'))}")
    return pwd_context.hash(password)

def verify_password(plain_pasword: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_pasword, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt

async def authenticate_user(username: str, password: str):
    user = await get_user_by_username(username)
    if not user or not verify_password(plain_pasword=password, hashed_password=user.password):
        return None
    return user
