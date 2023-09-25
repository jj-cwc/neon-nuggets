from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from money_type import MoneyType  # Ensure this is imported correctly if it is a custom type

from model_base import Base  # Importing Base from model_base.py

class Trader(Base):
    __tablename__ = 'traders'
    
    id = Column(Integer, primary_key=True)
    type = Column(String)  # Discriminator column to determine the type of trader (Bot/Player)
    cash_balance = Column(MoneyType, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'trader',
        'polymorphic_on': type
    }
    
    # Define relationships
    holdings = relationship('Holding', back_populates='trader')  # Ensure Holding is properly imported or defined

class Bot(Trader):
    __tablename__ = 'bots'
    
    id = Column(Integer, ForeignKey('traders.id'), primary_key=True)
    trading_frequency = Column(Integer)  # Values from 0 to 10
    risk_appetite = Column(Integer)  # Values from 0 to 10
    strategy_focus = Column(Integer)  # Values from 0 to 10
    holding_duration = Column(Integer)  # Values from 0 to 10
    reaction_to_market_news = Column(Integer)  # Values from 0 to 10
    __mapper_args__ = {
        'polymorphic_identity': 'bot',
    }

class Player(Trader):
    __tablename__ = 'players'
    
    id = Column(Integer, ForeignKey('traders.id'), primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)  # You should probably use hashed passwords in a real application
    email = Column(String, unique=True)
    __mapper_args__ = {
        'polymorphic_identity': 'player',
    }
