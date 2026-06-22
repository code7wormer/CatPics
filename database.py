from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



load_dotenv()
eng=create_engine(getenv("DB_URL"))
sesh=sessionmaker(autoflush=False,bind=eng)


