from datetime import datetime
from decimal import *

from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, create_engine, Numeric
from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# decimal operations settings
getcontext().prec = 6
getcontext().rounding = ROUND_HALF_UP
Base = declarative_base()

# customer has a one-to-many relationship with template, where customer is the parent
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    alias = Column(String)
    firm_name = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    tax_id = Column(String, nullable=False)
    address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    payment = Column(Boolean)
    template = relationship("Template")


# product has many-to-many relationship with template, where template is the parent
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    symbol = Column(String)
    unit = Column(String, nullable=False)
    unit_net_price = Column(Numeric(precision=2), nullable=False)
    vat_rate = Column(Numeric(precision=2), nullable=False)
    per_month = Column(Boolean, nullable=False)


class Settings(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)


class Numbering(Base):
    __tablename__ = "numbering"
    id = Column(Integer, primary_key=True)
    month = Column(Integer)
    number = Column(Integer)

    def __init__(self):
        self.date = datetime.now().month
        self.number = 1


# association table for the products-template many-to-many relationship
association_table = Table('association', Base.metadata,
                          Column('product_id', Integer, ForeignKey('products.id')),
                          Column('template_id', Integer, ForeignKey('template.id')))


# template implements one-to-many relationship with customer and many-to-many relationship with product
class Template(Base):
    __tablename__ = "template"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey(Customer.id))
    products = relationship("Product", secondary=association_table, uselist=False)
    quantity = Column(Numeric)
    net_val = Column(Numeric(precision=2))
    tax_val = Column(Numeric(precision=2))
    gross_val = Column(Numeric(precision=2))

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []
        self.quantity = Decimal(0.0)
        self.net_val = Decimal(0.0)
        self.tax_val = Decimal(0.0)
        self.gross_val = Decimal(0.0)


# TODO: implement listener
@event.listens_for(Template.quantity, "set")
def quantity_listener(target, value, oldvalue, initiator):
    print(target)
    print(initiator)
    print(oldvalue)
    print(value)
    # target.net_val =
    # target.tax_val =
    # target.gross_val =

engine = create_engine('sqlite:///invoices.db')

# Create a session to handle updates.
Session = sessionmaker(bind=engine)
# Initalize the database if it is not already.
Base.metadata.create_all(engine)
