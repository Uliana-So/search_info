import logging
import logging.config
from flask import Flask
from flask import request, jsonify, make_response
from urllib.parse import urlparse

from .db_connect import db_session
from .db_interplay import remove_post, search_post


logging.basicConfig(filename="/opt/search_info/logs/logger_web.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def remove(id: int):
    res_data = {
        "id": id,
        "removed": remove_post(id)
    }

    logging.info(res_data)
    return make_response(jsonify(res_data), 200)


def search(find_str: str):
    res_data = {
        "find": find_str,
        "count": 0,
        "results": []
    }

    data = search_post(find_str)
    if data:
        res_data["count"] = len(data)
        for item in data:
            struct_data = {
                "created_date": item.created_date,
                "post": item.text.rstrip(),
                "rubrics": item.rubrics.rstrip()
            }
            res_data["results"].append(struct_data)
    logging.info(res_data)
    return make_response(jsonify(res_data), 200)


@app.route("/find", methods=["GET"])
def read_request_find():
    try:
        data = urlparse(request.url).query.split("=")
        if data and len(data) == 2 and "search" in data:
            return search(data[1])

    except Exception as error:
        logging.error(error, exc_info=True)
        return make_response(jsonify(), 400)

    return make_response(jsonify(), 400)


@app.route("/remove", methods=["GET"])
def read_request_remove():
    try:
        data = urlparse(request.url).query.split("=")
        if (data and len(data) == 2 and "delete" in data and
                data[1].isdigit and int(data[1]) > 0):
            return remove(int(data[1]))

    except Exception as error:
        logging.error(error, exc_info=True)
        return make_response(jsonify(), 400)

    return make_response(jsonify(), 400)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
