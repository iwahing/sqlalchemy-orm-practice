from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///university.db"

# engine = create_engine(DATABASE_URL, echo=True)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

    # type_annotation_map = {
    # }
