import datetime

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String, create_engine, Boolean, inspect
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey

from baselayer.database import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)


class BaseMixin(Base):
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)

    __abstract__ = True

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"


class Category(BaseMixin):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # Define a one-to-many relationship with Product
    products = relationship("Product", back_populates="category")


class Product(BaseMixin):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Correct the relationship with the Category model
    category = relationship("Category", back_populates="products")

    # Correct the relationship with the Sale model
    sales = relationship("Sale", back_populates="product")

    # Define the relationship with the Inventory model
    inventory = relationship("Inventory", back_populates="product")


class Sale(BaseMixin):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    sale_date = Column(DateTime)
    quantity = Column(Integer)
    total_price = Column(Float)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates="sales")


class Inventory(BaseMixin):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    product = relationship("Product", back_populates="inventory")


# Optionally, create a session for further database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base.metadata.create_all(bind=engine)
