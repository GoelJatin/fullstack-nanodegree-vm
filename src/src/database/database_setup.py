"""Database setup for the Restaurant application."""

import os

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    create_engine
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Restaurant(Base):
    """Restaurant model."""
    __tablename__ = 'restaurant'

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(80),
        nullable=False
    )


class MenuItem(Base):
    """MenuItem model."""
    __tablename__ = 'menu_item'

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(80),
        nullable=False
    )

    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    restaurant_id = Column(
        Integer,
        ForeignKey('restaurant.id')
    )

    restaurant = relationship(Restaurant)


engine = create_engine(
    'postgresql+psycopg2://'
    f'{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}@'
    f'{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/'
    f'{os.getenv("DATABASE_NAME")}'
)

Base.metadata.create_all(engine)
