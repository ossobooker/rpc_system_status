from pydantic import BaseModel
from typing import Literal


class Status(BaseModel):
    hv: Literal["DG", "SG", "Gaps disconnected"]
    th: Literal["OK", "DT Line only", "No Threshold Control"]
    gas_leaking: Literal["Not Leaking", "Full Leak", "Medium Leak", "Small Leak"]
    gas_reapired_ls2: Literal["Yes", "No"]
    gas_line_splitted: Literal["Yes", "No"]
    strips_masked: Literal["Yes", "No"]
    chip_disabled: Literal["Yes", "No"]
    other: Literal["Yes", "No"]

    class Config:
        schema_extra = {
            "example": {
                "hv": "DG",
                "th": "OK",
                "gas_leaking": "Not Leaking",
                "gas_reapired_ls2": "No",
                "gas_line_splitted": "No",
                "strips_masked": "No",
                "chip_disabled": "No",
                "other": "No",
            }
        }
