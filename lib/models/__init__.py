from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up database URL (make sure to adjust it to your setup)
DATABASE_URL = "sqlite:///vote_sphere.db"

# Database setup
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Import models to ensure they are registered with Base
from .user import User
from .candidate import Candidate
from .vote import Vote
