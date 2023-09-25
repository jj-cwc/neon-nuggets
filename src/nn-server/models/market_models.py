from datetime import date
from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from model_base import Base
from money_type import MoneyType

class TradeVolume(Base):
    __tablename__ = 'trade_volumes'
    
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('assets.id'), nullable=False)
    date = Column(Date, default=date.today())
    volume = Column(Integer, default=0)
    
    # You can also add relationships if needed

class MarketStat(Base):
    __tablename__ = 'market_stats'
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True)
    total_volume = Column(Integer)
    total_transactions = Column(Integer)
    # Other aggregate market statistics as needed

class AssetStat(Base):
    __tablename__ = 'asset_stats'
    
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('assets.id'))
    date = Column(Date)
    opening_price = Column(MoneyType)
    closing_price = Column(MoneyType)
    high_price = Column(MoneyType)
    low_price = Column(MoneyType)
    volume = Column(Integer)
    # Other asset-specific statistics as needed
    
    asset = relationship('Asset', back_populates='asset_stats')

