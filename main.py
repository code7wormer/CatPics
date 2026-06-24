from fastapi import FastAPI,Depends,HTTPException
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
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

@app.delete("/product/{id}")
def delete_cat(id:int , db:Session=Depends(get_db)):
    tup=db.query(db_models.Cat).filter(db_models.Cat.id==id).first()
    if tup:
        db.delete(tup)
        db.commit()
        return {"message":"Product Deleted Successfully"}
    else:
        raise HTTPException(
            status_code=404,
            detail="Product Not found"
        )


@app.put("/product/{id}")
def update_cat(id:int,cat:CreatePic, db:Session=Depends(get_db)):
    tup=db.query(db_models.Cat).filter(db_models.Cat.id==id).first()
    if tup:
        tup.url=cat.url
        tup.desc=cat.desc
        tup.category=cat.category
        tup.type=cat.type
        tup.updated_at=datetime.now(UTC)
        db.commit()
        db.refresh(tup)
        return tup
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
@app.get("/products")
def load(db:Session=Depends(get_db)):
    return db.query(db_models.Cat).all()
