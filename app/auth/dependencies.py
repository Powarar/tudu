from uuid import UUID
from fastapi import Request, Depends, HTTPException, status
from jose import jwt, JWTError
from app.settings import settings
from app.repositories.users import get_user_by_uuid

async def get_current_user(request: Request):
    token = request.cookies.get("users_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authentificated")
    

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
        user_id = UUID(user_id)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return user_id