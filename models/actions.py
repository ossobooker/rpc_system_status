from datetime import datetime
from pydantic import BaseModel, AnyHttpUrl

# import uuid


class Action(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4)
    type: str
    set_status: str
    comment: str
    reporter: str
    elog: AnyHttpUrl
    date: datetime

    class Config:
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "type": "HV Operation Mode",
                "comment": "bla bla bla",
                "reporter": "Fulano",
                "date": 13,
            }
        }
