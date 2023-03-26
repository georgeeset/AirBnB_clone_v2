#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


one_many = "all, delete"


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship(
        'Place',
        cascade=one_many,
        backref='user'
    )
    reviews = relationship(
        'Review',
        cascade=one_many,
        backref='user'
    )
