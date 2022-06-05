from elasticsearch import Elasticsearch
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
import pandas as pd


url = "postgresql+psycopg2://{}:{}@{}/{}".format("app_connector",
                                                 "124qwerty124",
                                                 "postgres",
                                                 "forum")
engine = create_engine(url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rubrics = Column(Integer, unique=True)
    text = Column(String)
    created_date = Column(DateTime)


def create_table():
    insp = inspect(engine)
    if insp.has_table("posts"):
        return False
    df = pd.read_csv("posts.csv")
    df.to_sql("posts", engine, index_label='id')
    return True


def main():
    if create_table():
        es = Elasticsearch('http://elasticsearch:9200')
        data = db_session.query(Posts).all()
        for item in data:
            es.index(index="posts", id=item.id, body={"text": item.text.rstrip()})


if __name__ == "__main__":
    main()
