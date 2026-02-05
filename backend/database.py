from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "sqlite:///./quiz.db" #creates a quiz.db file if doent exist if exist it connects to it 

#connecting to data base
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

#creating a databse session
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()