#!/usr/bin/env python3
"""list all documents"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """list all docs in mongo_collection"""
    schools = mongo_collection.find()
    if schools:
        return schools
    return []
