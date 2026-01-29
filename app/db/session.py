from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

try:
    engine = create_engine(settings.DATABASE_URL)
except Exception as e:
    print(f"Failed to connect to DB, {str(e)}")
    raise
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Database connection failed, {str(e)}")
        raise
    finally:
        db.close()