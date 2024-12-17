from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    posts = relationship("Post", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, content={self.content})>"
