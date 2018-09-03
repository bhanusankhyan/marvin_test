from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    password = Column(String(50), nullable = False)
    mobileNumber = Column(Integer, primary_key = True)



engine = create_engine('sqlite:////home/bhanu/Documents/final_build/flask7/marvin_test/marvin.db')
Base.metadata.create_all(engine)
