from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from money_type import MoneyType  # Ensure this is imported correctly if it is a custom type
#from trader_models import Trader
from datetime import datetime

from model_base import Base  # Importing Base from model_base.py

class Asset(Base):
    __tablename__ = 'assets'
    
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)  # Associated Company
    quantity_available = Column(Integer, nullable=False, default=0)
    last_traded_price = Column(MoneyType, nullable=False)
    last_traded_at = Column(DateTime, nullable=True)
    asset_stats = relationship('AssetStat', back_populates='asset')
    
    # Define relationships
    company = relationship('Company', back_populates='assets')  # Ensure Company is properly imported or defined
    orders = relationship('Order', back_populates='asset')  # Ensure Order is properly imported or defined
    holdings = relationship('Holding', back_populates='asset')

class Holding(Base):
    __tablename__ = 'holdings'
    
    id = Column(Integer, primary_key=True)
    trader_id = Column(Integer, ForeignKey('traders.id'), nullable=False)  # Associated Trader
    asset_id = Column(Integer, ForeignKey('assets.id'), nullable=False)  # Associated Asset
    quantity = Column(Integer, nullable=False)
    acquired_price = Column(MoneyType, nullable=False)
    acquired_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Define relationships
    trader = relationship('Trader', back_populates='holdings')  # Ensure Trader is properly imported or defined
    asset = relationship('Asset', back_populates='holdings')

