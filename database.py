from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_DATABASE_URL = 'mysql://monty:montypassword@localhost/veterinariamercy'

engine = create_engine(_DATABASE_URL)
results = engine.engine.execute('select * from PRODUCTO')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

