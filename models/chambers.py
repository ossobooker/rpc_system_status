from typing import List
from pydantic import BaseModel, Field
import uuid

from models import Action
from models import Status


class Chamber(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    barrel_or_endcap: str
    wheel_or_disk: int
    station_ring: int
    sector: int
    status: Status
    actions: List[Action]

    class Config:
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "W+3_S13_RB5out",
                "barrel_or_endcap": "barrel",
                "wheel_or_disk": 3,
                "station_ring": 5,
                "sector": 13,
                "status": {
                    "hv": "DG",
                    "th": "OK",
                    "gas_leaking": "Not Leaking",
                    "gas_reapired_ls2": "No",
                    "gas_line_splitted": "No",
                    "strips_masked": "No",
                    "chip_disabled": "No",
                    "other": "No",
                },
                "actions": [],
            }
        }
