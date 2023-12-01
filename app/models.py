import datetime
import sqlalchemy as sq

from sqlalchemy import DateTime, ForeignKey, String, creat_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True, nullable=False)
    password = sq.Column(sq.String(70), nullable=False)
    email = sq.Column(sq.String(length=40), index=True, unique=True)


class Advertisement(Base):
    __tablename_- = "advertisement"
    
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=20))
    description = sq.Column(sq.String(length=240))
    date_post = sq.Column(sq.DateTime)
