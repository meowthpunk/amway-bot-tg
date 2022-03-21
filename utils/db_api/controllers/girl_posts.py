from utils.db_api.main_db import Session
from utils.db_api.models import GirlPost


def get_all_posts(session: Session):
    return session.query(GirlPost).all()


def get_post(session: Session, post_id):
    return session.query(GirlPost).filter(GirlPost.id == post_id).first()
