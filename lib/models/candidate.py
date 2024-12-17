from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .. import Base  # Import Base from the parent module

class Candidate(Base):
    __tablename__ = 'candidates'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    votes = relationship("Vote", back_populates="candidate")

    def __repr__(self):
        return f"<Candidate(id={self.id}, name={self.name})>"
