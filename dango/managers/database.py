import psycopg2
import dango
from projects.DangoBot.dango.config import db_user

'''
CREATE TABLE Users (
    id            not null
    name          text not null
    zid           char (8)
    bal           integer default 100
    primary key   (id)
)
'''

def __init__():
    try:
        db = psycopg2.connect(
            host = dango.config.db_host(),
            dbname = dango.config.db_database(),
            user = dango.config.db_user(),
            password = dango.config.password(),
        )
        return db
    except Exception as err:
        print("\n[!] Unable to connect to database!\n {}".format(err))
        quit()

def db_cursor(db):
    try:
        return db.cursor()
    except Exception as err:
        print("\n[!] Unable to create cursor!\n {}".format(err))

def add_user(db, user):
    try:
        db.cursor.execute(
            "INSERT INTO Users (id, name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE name = %s",
            (user.id, user.name)
        )
        db.commit()
    except Exception as err:
        print("\n[!] Unable to add user!\n {}".format(err))