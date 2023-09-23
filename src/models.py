import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

    username = Column (String (80), nullable=False)
    email = Column(String(256), nullable=False, unique=True)

class Post(Base):
    __tablename__ = 'post'
   
    id = Column(Integer, primary_key=True)

    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)

    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    post_id = Column (Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)

    type = Column(Enum, nullable=False)
    url = Column(String(8000), nullable=False)

    post_id = Column (Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)

    user_from_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    user = relationship(User)

    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
