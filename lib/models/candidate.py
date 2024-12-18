from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base  # Assuming Base is imported from lib.models

class Candidate(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    votes = relationship("Vote", back_populates="candidate")

    def __repr__(self):
        return f"<Candidate(id={self.id}, name={self.name})>"
