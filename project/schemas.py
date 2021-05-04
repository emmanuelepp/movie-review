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


class ResponseModel(BaseModel):

    class Config:
        orm_mode = True
        getter = PeeWeeGetterDict


class UserResponseModel(ResponseModel):
    id: int
    username: str

# --------Movie----------


class MoviewResponseModel(ResponseModel):
    id: int
    title: str


# --------Review----------


class ReviewValidator():

    @validator('score')
    def username_validator(cls, score):
        if score < 1 or score > 5:
            raise ValueError(
                "The score  must be more that 1 and less that 5")

        return score


class ReviewRequestModel(BaseModel, ReviewValidator):
    user_id: int
    movie_id: int
    review: str
    score: int


class ReviewResponseModel(ResponseModel):
    id: int
    movie: MoviewResponseModel
    reviews: str
    score: int


class ReviewRequestPutModel(BaseModel, ReviewValidator):
    reviews: str
    score: int
