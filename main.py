from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import db_models
from database import eng,sesh
from models import CreatePic
from datetime import datetime,UTC
app=FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://127.0.0.1:5500","http://localhost:5500"],
                   allow_methods=["*"],
                   allow_headers=["*"])


db_models.Base.metadata.create_all(bind=eng)
def get_db():
    db=sesh()
    try:
        yield db
    finally:
        db.close()

@app.post("/products")
def add_product(cat:CreatePic,db:Session=Depends(get_db)):
    tup=db_models.Cat(
        **cat.model_dump(),
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC)
    )
    db.add(tup)
    db.commit()
    db.refresh(tup)
    return tup

@app.get("/product/{id}")
def view_single_cat(id:int,db:Session=Depends(get_db)):
    tup=db.query(db_models.Cat).filter(db_models.Cat.id==id).first()
    if tup:
        return tup
    else:
        return "PRODUCT NOT FOUND"

