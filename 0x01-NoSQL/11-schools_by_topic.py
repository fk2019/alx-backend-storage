#!/usr/bin/env python3
"""find schools by given topic"""


def schools_by_topic(mongo_collection, topic):
    """find schools by given topic"""
    return mongo_collection.find({"topics": topic})
