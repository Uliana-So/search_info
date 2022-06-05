from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .db_config import read_config


params = read_config()
url = "postgresql+psycopg2://{}:{}@{}/{}".format(params["user"],
                                                 params["password"],
                                                 params["host"],
                                                 params["database"])
engine = create_engine(url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
