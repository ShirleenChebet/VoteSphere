from sqlalchemy import Column, Integer, String, relationship
from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    votes = relationship("Vote", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name})>"
