from .database import Base
from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey, TIMESTAMP, Float, JSON
from sqlalchemy.sql import func
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255))
    price = Column(Float)
    discountPercentage = Column(Float)
    rating = Column(Float)
    stock = Column(Integer)
    brand = Column(String(100))
    category = Column(String(100))
    thumbnail = Column(String(255))
    images = Column(JSON)  # Almacena las imágenes como JSON

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2))
    thumbnail = Column(String(255))
    sale_date = Column(TIMESTAMP, server_default=func.now())
