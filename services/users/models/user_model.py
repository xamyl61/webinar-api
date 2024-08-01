from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.dataclasses import dataclass


class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    uuid: str

    # model_config = ConfigDict(extra='forbid')

    @field_validator("email", "name", "nickname", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
