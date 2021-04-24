from pydantic import BaseModel
from pydantic import validator


class UserBaseModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 4 or len(username) > 50:
            raise ValueError(
                "The len of user name must be more that 4 and less that 50")

        return username
