
from sqlalchemy import Integer, String, Text, Table, Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .database import Base


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True, index=True)
    quote_text = Column(Text, index = True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="quotes")
    tags = relationship("Tag", secondary='quote_tags', back_populates="quotes")


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_date = Column(String, index=True)
    birth_place = Column(String, index=True)
    biography = Column(Text)
    quotes = relationship("Quote", back_populates="author")


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quotes = relationship("Quote", secondary='quote_tags', back_populates="tags")


quote_tags = Table('quote_tags', Base.metadata,
    Column('quote_id', Integer, ForeignKey('quotes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id')),
    UniqueConstraint('quote_id', 'tag_id', name='uq_quote_tag'))

