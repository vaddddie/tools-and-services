from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine(f'sqlite:///app/models/database.db', echo=False)

Session = sessionmaker(bind=engine)
    

