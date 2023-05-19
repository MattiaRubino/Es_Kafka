from sqlalchemy import CHAR, Column, DateTime, Numeric, String, Table
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
metadata = Base.metadata

class Document(Base):
    __tablename__ = 'documents'

    id_document = Column(Numeric, primary_key=True,nullable=False)
    author = Column(String)
    title_book = Column(String)
    date = Column(DateTime)
    e_mail = Column(String)

class Log_change(Base):

    __tablename__ = 'log_change'
    id_document = Column(Numeric)
    type_chage = Column(String)
    date_change = Column(DateTime,)
    id_change = Column(Numeric, primary_key=True)

