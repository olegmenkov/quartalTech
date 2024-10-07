from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Apartment(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    area = Column(Float)
    rooms = Column(Integer)
    estimated_price = Column(Float)

    listings = relationship("Listing", back_populates="apartment")


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    apartment_id = Column(Integer, ForeignKey("apartments.id"))

    apartment = relationship("Apartment", back_populates="listings")
