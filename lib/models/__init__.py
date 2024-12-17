from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .user import User
from .candidate import Candidate
from .vote import Vote

# Database setup
DATABASE_URL = "sqlite:///your_database.db"  # Use your actual database URL here
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()
