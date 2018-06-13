import os

from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

def get_engine(sqlalchemy_url):
    if sqlalchemy_url == "sqlite:///:memory:":
        import sqlite3
        params = { 'uri': True }
        creator = lambda: sqlite3.connect('file::memory:?cache=shared', **params)
        return create_engine(sqlalchemy_url, creator=creator)
    else:
        return create_engine(sqlalchemy_url)        

engine = get_engine(os.environ['SQLALCHEMY_URL'])

Session = scoped_session(sessionmaker(bind=engine))
