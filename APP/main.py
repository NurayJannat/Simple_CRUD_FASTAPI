from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sqlalchemy import create_engine

from . import crud, models, schemasa
# from crud import *
# from models import *
# from schemasa import *

from .database import SessionLocal, engine



# def create_db(url: str):
#     engine = create_engine(
#         url,
#         connect_args={"check_same_thread": False},
#         native_datetime=True,
#     )
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     Base.metadata.create_all(bind=engine)

#     return SessionLocal


# SessionLocal = create_db("sqlite:///./real.db")
# models.Base.metadata.create_all(bind=engine)



models.Base.metadata.create_all(bind=engine)


app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------------------------    Parent User Section ----------------------------------------------------------


@app.post("/parents/")
def create_user(parent: schemasa.ParentCreate, db: Session = Depends(get_db)):
    return crud.create_parent(db=db, parent=parent)


@app.get("/parents/")
def read_parents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print("enter the url")
    parents = crud.get_parents(db, skip=skip, limit=limit)
    print("parents: ", parents)
    return parents


@app.put("/parents/{parent_id}")
def update_parent(parent_id: int, parent_update: schemasa.Parent, db: Session = Depends(get_db)):
    update_result = crud.update_parent(db=db, parent_id=parent_id, parent_update=parent_update)

    return update_result

@app.delete("/parents/{parent_id}")
def delete_parent(parent_id: int, db: Session = Depends(get_db)):
    print("delete parent, ", parent_id)
    db_result = crud.delete_parent(db, parent_id=parent_id)

    return db_result


# -------------------------------------------    Child User Section ----------------------------------------------------------
    

@app.post("/child/")
def create_child(child: schemasa.ChildCreate, db: Session = Depends(get_db)):
    print("create child", child)

    return crud.create_parent_child(db=db, child=child)


@app.get("/child/")
def read_child(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    children = crud.get_children(db, skip=skip, limit=limit)
    return children


@app.put("/child/{child_id}")
def update_child(child_id: int, child_update: schemasa.Child, db: Session = Depends(get_db)):
    update_result = crud.update_child(db=db, child_id=child_id, child_update=child_update)

    return update_result

@app.delete("/child/{child_id}")
def delete_child(child_id: int, db: Session = Depends(get_db)):
    db_result = crud.delete_child(db, child_id=child_id)

    return db_result



# @app.get("/clear_db")
# def clear_db(db: Session = Dep):
    