from elasticsearch import Elasticsearch
from flask import jsonify, make_response

from .db_connect import db_session
from .model import Posts


def remove_post(id: int) -> bool:
    es = Elasticsearch("http://elasticsearch:9200")
    data = db_session.query(Posts).get(id)

    if data:
        db_session.delete(data)
        es.delete(index="posts", id=id)
        db_session.commit()
        return True

    return False


def search_post(find_word: str):
    res_id = []
    es = Elasticsearch("http://elasticsearch:9200")
    resp = es.search(index="posts",
                     body={"query": {
                             "match": {
                                "text": find_word
                                }
                             }
                           })
    hits_data = resp["hits"]["hits"]
    for item in hits_data:
        res_id.append(item["_id"])
    if res_id:
        return db_session.query(Posts).filter(Posts.id.in_(res_id)).order_by(Posts.created_date).limit(20).all()
    return None
