from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base  # Assuming Base is imported from lib.models

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    votes = relationship("Vote", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
