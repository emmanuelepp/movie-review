from pydantic import BaseModel
from pydantic import validator
from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect


class PeeWeeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):

        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res


class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 4 or len(username) > 50:
            raise ValueError(
                "The len of user name must be more that 4 and less that 50")

        return username


class UserResponseModel(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
        getter = PeeWeeGetterDict
