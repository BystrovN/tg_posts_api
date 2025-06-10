from pydantic import BaseModel, constr


class RegisterSchema(BaseModel):
    username: constr(min_length=3)
    password: constr(min_length=6)


class TokenSchema(BaseModel):
    token: str
