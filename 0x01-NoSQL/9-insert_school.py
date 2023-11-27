#!/usr/bin/env python3
"""insert into a collection"""


def insert_school(mongo_collection, **kwargs):
    """insert into school"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
