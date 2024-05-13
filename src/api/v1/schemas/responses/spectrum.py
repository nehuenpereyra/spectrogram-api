from pydantic import BaseModel
from typing import List


class Predictions(BaseModel):
    x: float
    y: float
    w: float
    h: float


class PredictionsResponse(BaseModel):
    predictions: List[Predictions]

    class Config:
        json_schema_extra = {
            "example": {
                "predictions": [
                    {
                        "x": 0.521484375,
                        "y": 0.919921875,
                        "w": 0.94140625,
                        "h": 0.16015625
                    }
                ]
            }
        }
