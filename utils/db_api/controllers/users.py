from utils.db_api.controllers.utils import add_row_to_db
from utils.db_api.main_db import Session
from utils.db_api.models import User


def validate_and_add_user(session: Session, user):
    user_query = session.query(User).filter(User.user_id == user.user_id)
    if not user_query.first():
        add_row_to_db(session, user)


def get_user(session: Session, user):
    return session.query(User).filter(User.user_id == user).first()
