from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    userName = Column(String(50), nullable = False)
    mobileNumber = Column(Integer, primary_key = True)



engine = create_engine('sqlite:////home/bhanu/Documents/final_build/flask2/marvin1.db')
Base.metadata.create_all(engine)
