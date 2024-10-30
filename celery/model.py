# model.py
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///launches.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Launch(Base):
    __tablename__ = 'launches'

    id = Column(String, primary_key=True, index=True)  # SpaceX launch ID
    name = Column(String)  # Title of the launch
    details = Column(Text)  # Details of the launch
    success = Column(Boolean)  # Whether the launch was successful
    date_utc = Column(DateTime)  # UTC date of the launch
    rocket_id = Column(String)  # ID of the rocket used
    failures = Column(Text)  # Description of failures, if any
    web_url = Column(String)  # URL to the launch's web page

Base.metadata.create_all(bind=engine)
