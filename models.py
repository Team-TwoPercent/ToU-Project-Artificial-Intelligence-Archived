from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base



class Check(Base):
    __tablename__ = 'check'

    content = Column(String, unique=True, nullable=False)
    true_check = Column(Integer, nullable=False)



