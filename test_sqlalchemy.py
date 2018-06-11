from flask_sqlalchemy_starter.models import Message
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("postgresql://vlad:simple@localhost/TestDB", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

hi_message = Message(message="hi", new_field="garbage")

session.add(hi_message)
session.commit()
