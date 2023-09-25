from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import all model classes
# this will generate warnings because they're not used, but
# that's ok, because with these imports here, they can all be directly
# imported from model, rather than from their individual files 
from model_base import Base
from trader_models import Trader, Bot, Player
from asset_models import Asset, Holding
from order_models import Order, OrderType, OrderStatus
from company_models import Company, Sector

# Setup engine and create tables
engine = create_engine('sqlite:///neon-nuggets.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# This file can be executed to initialize the database and can also be imported to get access to all model classes
