from typing import List, Union

from pydantic import BaseModel


# ----------------------------------  Child User Section ---------------------------------------------

class ChildBase(BaseModel):
    first_name: str
    last_name: str


class ChildCreate(ChildBase):
    parent_id: str

    


class Child(ChildBase):
    parent_id: int

    class Config:
        orm_mode = True


# -------------------------------------- Parent User Section ---------------------------------------

class ParentBase(BaseModel):
    first_name: str
    last_name: str
    address: str


class ParentCreate(ParentBase):
    pass


class Parent(ParentBase):
    pass

    class Config:
        orm_mode = True

