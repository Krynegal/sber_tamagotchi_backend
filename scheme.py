from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    UserId: str
    name: str
    foodLevel: int
    sleepLevel: int
    playLevel: int
    timeOfExit: datetime
    sec: int
    min: int
    hour: int
    kusua: bool
    flag: bool
    
class Item(BaseModel):
    UserId: str
    name: str
    foodLevel: int
    playLevel: int
    sleepLevel: int
    timeOfExit: datetime
    sec: int
    min: int
    hour: int
    kusua: bool
    flag: bool
