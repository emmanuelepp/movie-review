from fastapi import HTTPException
from fastapi import APIRouter
from ..database import User
from ..schemas import UserRequestModel
from ..schemas import UserResponseModel

router = APIRouter(prefix='/api/v1/users')


@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).exists():

        return HTTPException(409, 'User name already exist.')

    hash_pssword = User.encrypt_password(user.password)

    user = User.create(
        username=user.username,
        password=hash_pssword
    )

    return user
