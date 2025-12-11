from fastapi import APIRouter, HTTPException

from app.api.deps import get_current_user, CurrentUserDep, SessionDep
from app.models.users import UserCreate, UserUpdate, UserOut
from app.repositories.users import (create_user as create_user_repo,
    update_user as update_user_repo,
    get_user_by_username,
    get_user_by_id)

router = APIRouter(prefix='/users', tags=['users'])

# получить текущего пользователя
@router.get(path='/me', response_model=UserOut)
async def get_user_me(current_user: CurrentUserDep):
    return current_user

@router.get(path='/username', response_model=UserOut)
async def get_user(session: SessionDep, username: str):
    user = await get_user_by_username(session, username)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.post(path='/', response_model=UserOut)
async def create_user(session: SessionDep, user_data: UserCreate):
    new_user = await create_user_repo(session, user_data)
    return new_user

@router.put(path='/{user_id}', response_model=UserOut)
async def update_user(user_id: int, user_data: UserUpdate, session: SessionDep) -> UserOut:
    user_db = await get_user_by_id(session, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail='User not found')
    updated_user = await update_user_repo(session, user_db, user_data)
    return updated_user