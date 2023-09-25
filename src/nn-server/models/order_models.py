from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from datetime import datetime
from money_type import MoneyType  # Make sure to import it correctly if it is a custom type

from model_base import Base  # Importing Base from model_base.py

class OrderType(PyEnum):  # Changed Enum to PyEnum to avoid conflict with sqlalchemy Enum
    MARKET = "Market Order"
    LIMIT = "Limit Order"
    STOP = "Stop Order"
    STOP_LIMIT = "Stop-Limit Order"
    TRAILING_STOP = "Trailing Stop Order"

class OrderStatus(PyEnum):  # Changed Enum to PyEnum to avoid conflict with sqlalchemy Enum
    PENDING = "Pending"
    MATCHED = "Matched"
    EXECUTED = "Executed"
    CANCELLED = "Cancelled"

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    trader_id = Column(Integer, ForeignKey('traders.id'), nullable=False)
    asset_id = Column(Integer, ForeignKey('assets.id'), nullable=False)
    order_type = Column(Enum(OrderType), nullable=False)
    order_status = Column(Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(MoneyType, nullable=False)  # Ensure you have the MoneyType properly imported
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Define relationships
    trader = relationship('Trader', back_populates='orders')  # Ensure Trader is properly imported or defined
    asset = relationship('Asset', back_populates='orders')  # Ensure Asset is properly imported or defined
