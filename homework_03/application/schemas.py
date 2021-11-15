from pydantic import BaseModel


class PingBase(BaseModel):
    message: str = "pong"


class PingOut(PingBase):
    pass
