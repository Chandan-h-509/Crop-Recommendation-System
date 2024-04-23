from pydantic import BaseModel

class Crop(BaseModel):
    N:int
    P:int
    K:int
    temperature:float
    humidity:float
    ph:float
    rainfall:float