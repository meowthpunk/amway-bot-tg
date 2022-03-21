from utils.db_api.main_db import Session


def add_row_to_db(session: Session, row):
    session.add(row)
    session.commit()
