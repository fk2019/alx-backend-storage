#!/usr/bin/env python3
"""update all topics"""

def update_topics(mongo_collection, name, topics):
    """ update topics"""
    result = mongo_collection.update_one(
        {"name": name}, {"$set": {"topics": topics}})
    return result
