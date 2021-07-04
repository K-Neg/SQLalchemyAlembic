import sqlalchemy
from decouple import config
import logging

# URL from .env
SQLALCHEMY_DATABASE_URL = config("DATABASE_URL")

engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)


async def retrieve_all_users():
    """"""
    query = sqlalchemy.text("SELECT * FROM users")
    try:
        with engine.connect() as con:
            users = con.execute(query).fetchall()
    except Exception as consultError:
        logging.warn(consultError)
        users = None
    finally:
        return users
