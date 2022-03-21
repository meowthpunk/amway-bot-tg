from utils.db_api.controllers.utils import add_row_to_db
from utils.db_api.main_db import Session
from utils.db_api.models import UserPost


def add_user_post_rel(session: Session, user_id, post_id):
    user_post_rel = UserPost(
        user=user_id,
        post=post_id,
    )
    add_row_to_db(session, user_post_rel)


def get_user_watched_posts(session: Session, user):
    users_posts_query = session.query(UserPost).filter(UserPost.user == user)
    users_posts = [post.post for post in users_posts_query]
    return users_posts


def delete_relationship_rows(session: Session, user):
    session.query(UserPost).filter(UserPost.user == user). \
        delete(synchronize_session=False)
    session.commit()
