import os
import logging
from configparser import ConfigParser


def read_config():
    db = {}

    try:
        filename = os.environ["DB_FILE"]
        section = "postgresql"
        parser = ConfigParser()
        parser.read(filename)
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    except Exception:
        logging.error("Error data for database")

    return db
