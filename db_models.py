from sqlalchemy import Column,Integer,Text,String,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class Cat(Base):
    __tablename__ = "Cats"
    id=Column(Integer,primary_key=True)
    url=Column(String)
    desc=Column(String)
    category=Column(String)
    type=Column(String)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)