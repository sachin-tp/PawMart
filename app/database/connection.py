from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings

engine = create_engine(settings.DATABASE_URL)

SessiionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessiionLocal()
    try:
        yield db
    finally:
        db.close()

