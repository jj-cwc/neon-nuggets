from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from model_base import Base, MoneyType
#from asset_models import Asset  # Importing Asset from asset_models.py

class HistoricalData(Base):
    __tablename__ = 'historical_data'
    
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('assets.id'), nullable=False)  # ForeignKey referencing to Asset
    date = Column(Date, nullable=False)
    open_price = Column(MoneyType, nullable=False)
    close_price = Column(MoneyType, nullable=False)
    high_price = Column(MoneyType, nullable=False)
    low_price = Column(MoneyType, nullable=False)
    volume = Column(Integer, nullable=False)
    
    asset = relationship('Asset', back_populates='historical_data')  # Relationship with Asset

# Later on, you can add more classes/models as needed, related to brokerage activities.
