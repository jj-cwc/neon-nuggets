from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_base import Base  # Importing Base from model_base.py

class Sector(Base):
    __tablename__ = 'sectors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    companies = relationship('Company', back_populates='sector')

class Company(Base):
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ticker_symbol = Column(String)
    sector_id = Column(Integer, ForeignKey('sectors.id'))
    sector = relationship('Sector', back_populates='companies')
    
    bio = Column(String)
    volatility = Column(Integer)
    growth = Column(Integer)
    transparency = Column(Integer)
    dividend_policy = Column(Integer)
    ethical_stance = Column(Integer)
