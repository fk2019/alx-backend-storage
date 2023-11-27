#!/usr/bin/env python3
"""return all students by avg score"""


def top_students(mongo_collection):
    """return top avg students"""
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
