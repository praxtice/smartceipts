from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Time, Boolean, Float
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("localhost://")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    validated = Column(Boolean)

class Location(Base):
    address = Column(String)
    coordinates = Column(String)

class Item(Base):
    __tablename__ = 'items'
    name = Column(String)
    brand = Column(String)

class Good(Base):
    __tablename__ = 'goods'
    item = relationship(Item)
    cart_id = Column(Integer)
    price = Column(Float)
    abbreviation = Column(String)
    location = relationship(Location)

class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column(Integer, primary_key=True)
    cart_id  = Column(Integer, autoincrement=True)
    location = Column(String)
    time = Column(Time)
    user = relationship(User)

class RecToCart(Base):
    cart_id = Column(Integer)
    rec_id  = Column(Integer)

def BuildCart(location: str, user: User, **kwargs):


def insert(item: Base) -> bool:
    session.add(item)

def commit() -> bool:
    session.commit()