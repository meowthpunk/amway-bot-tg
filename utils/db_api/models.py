from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    username = Column(String)
    first_name = Column(String)


class GirlPost(Base):
    __tablename__ = "girl_post"
    id = Column(Integer, primary_key=True)
    file_id = Column(String)
    text = Column(String)


class UserPost(Base):
    __tablename__ = "user_post_rel"
    id = Column(Integer, primary_key=True)
    user = Column(Integer)
    post = Column(Integer)
