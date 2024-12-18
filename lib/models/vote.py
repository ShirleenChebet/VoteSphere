from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from lib.models import Base  # Assuming Base is imported from lib.models

class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    candidate_id = Column(Integer, ForeignKey('candidates.id'), nullable=False)

    user = relationship("User", back_populates="votes")
    candidate = relationship("Candidate", back_populates="votes")

    def __repr__(self):
        return f"<Vote(id={self.id}, user_id={self.user_id}, candidate_id={self.candidate_id})>"
