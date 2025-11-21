from fastapi import APIRouter, HTTPException, status,Response

from app.auth.users import get_password_hash
from app.repositories.users import get_user_by_username, create_or_update_user
from app.schemas.users import UserRegister, UserLogin
from app.auth.users import authenticate_user, create_access_token

router = APIRouter(prefix='/auth', tags=['Auth'])



@router.post('/register')
async def register_user(user_data: UserRegister) -> dict:



    user = await get_user_by_username(username=user_data.username)
    if user:
        raise  HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    await create_or_update_user(user_dict)
    return {"message": "Вы успешно зарегистрированы!"}


@router.post('/login')
async def auth_user(response: Response, user_data: UserLogin):
    user = await authenticate_user(username=user_data.username, password=user_data.password)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверное имя пользователя или пароль')
    
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}