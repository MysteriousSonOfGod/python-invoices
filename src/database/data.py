from datetime import datetime

from sqlalchemy import event
from sqlalchemy.orm import relationship, exc, column_property, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.query import Query as _Query
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, UniqueConstraint, create_engine, Numeric
from decimal import *

# decimal operations settings
getcontext().prec = 6
getcontext().rounding = ROUND_HALF_UP

engine = create_engine('sqlite:///invoices.db')
Base = declarative_base()

# Initalize the database if it is not already.
Base.metadata.create_all(engine)

# Create a session to handle updates.
Session = sessionmaker(bind=engine)

# customer has a one-to-one relationship with template, where customer is the parent
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
    template = relationship("Template", uselist=False, back_populates="customer")

# product has many-to-many relationship with template, where template is the parent
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    symbol = Column(String)
    unit = Column(String, nullable=False)
    unit_net_price = Column(Numeric, nullable=False)
    vat_rate = Column(Numeric, nullable=False)
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
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('template_id', Integer, ForeignKey('template.id'))
)

# template implements one-to-one relationship with customer and many-to-many relationship with product
class Template(Base):
    __tablename__ = "template"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="template")
    products = relationship("Product", secondary=association_table)
    quantity = Column(Numeric)
    net_val = Column(Numeric)
    tax_val = Column(Numeric)
    gross_val = Column(Numeric)

    # TODO: implement constructor
    def __init__(self, **kwargs):
        self.quantity = Decimal(0.0)
        self.net_val = Decimal(0.0)
        self.tax_val = Decimal(0.0)
        self.gross_val = Decimal(0.0)


# TODO: implement listener
@event.listens_for(Template.quantity, "set")
def quantity_listener(target, value, oldvalue, initiator):
    print(target)
    print(initiator)
    # target.net_val =
    # target.tax_val =
    # target.gross_val =