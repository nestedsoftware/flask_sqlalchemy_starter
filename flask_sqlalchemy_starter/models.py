from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)
    message = Column(String)
    new_field = Column(String)
    
    def __repr__(self):
        return "<Message(message='%s', new_field='%s'>" % (self.message, self.new_field)
