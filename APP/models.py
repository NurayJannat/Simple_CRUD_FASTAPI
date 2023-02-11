from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from .database import Base

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str


class Parent(Base):
    __tablename__ = 'parent_table'

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    address = Column(String, index=True)

    children = relationship("Child")


class Child(Base):
    __tablename__ = "child_table"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    
    parent_id = Column(Integer, ForeignKey("parent_table.id"))
    