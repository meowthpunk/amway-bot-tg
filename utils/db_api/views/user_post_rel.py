from utils.db_api.controllers.girl_posts import get_all_posts
from utils.db_api.controllers.user_post_rel import get_user_watched_posts, delete_relationship_rows
from utils.db_api.main_db import Session


def is_posts_available(user_id):
    posts_id = [post.id for post in get_all_posts(Session())]
    users_posts = get_user_watched_posts(Session(), user_id)
    if len(posts_id) > len(users_posts):
        return True
    else:
        return False


def delete_relationships(user):
    delete_relationship_rows(Session(), user)
