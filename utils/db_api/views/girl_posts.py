import random

from utils.db_api.controllers.girl_posts import get_all_posts, get_post
from utils.db_api.controllers.utils import add_row_to_db
from utils.db_api.controllers.user_post_rel import get_user_watched_posts, add_user_post_rel
from utils.db_api.models import GirlPost
from utils.db_api.main_db import Session
from utils.db_api.views.user_post_rel import is_posts_available


def create_girl_post(file_id, text):
    post = GirlPost(
        file_id=file_id,
        text=text,
    )
    add_row_to_db(Session(), post)


def get_girl_post(user):
    if is_posts_available(user):
        posts_id = [post.id for post in get_all_posts(Session())]
        users_posts = get_user_watched_posts(Session(), user)
        available_posts = [posts for posts in posts_id if posts not in users_posts]

        post_id = random.choice(available_posts)

        text = get_post(Session(), post_id).text
        photo_url = get_post(Session(), post_id).file_id

        add_user_post_rel(Session(), user, post_id)
        return dict(
                        text=text,
                        photo_url=photo_url,
                    )
    else:
        return 'error'
