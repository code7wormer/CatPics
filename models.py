from pydantic import BaseModel
from enum import Enum
class Catype(str,Enum):
    white="white"
    black="black"
    spotted="spotted"
    ginger="ginger"

class CreatePic(BaseModel):
    url:str
    desc:str
    category:str
    type:Catype
