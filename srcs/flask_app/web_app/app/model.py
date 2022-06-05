from sqlalchemy import Column, Integer, String, DateTime

from .db_connect import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rubrics = Column(String, unique=True)
    text = Column(String)
    created_date = Column(DateTime)
