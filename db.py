from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DESTINATION_DB = f'postgresql+psycopg2://postgres:onibur@localhost:5432/Docomunet_book'
destination_engine = create_engine(DESTINATION_DB)
DestinationSession = sessionmaker(bind=destination_engine)
