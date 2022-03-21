from utils.db_api.controllers.users import validate_and_add_user
from utils.db_api.models import User
from utils.db_api.main_db import Session


def create_new_user(user_id, username, first_name):
    user = User(
        user_id=user_id,
        username=username,
        first_name=first_name,
    )
    validate_and_add_user(Session(), user)
