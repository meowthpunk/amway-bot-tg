from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, GirlPost, UserPost

# =====================
# use code in controllers only for queries in db
# code in views is open interfaces for bot
# =====================

DATABASE_NAME = 'amway.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)


def create_db():
    Base.metadata.create_all(engine)
