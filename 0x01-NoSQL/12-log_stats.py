#!/usr/bin/env python3
"""log nginx logs"""
from pymongo import MongoClient

if __name__ == "__main__":
    with MongoClient() as client:
        collection = client.logs.nginx
        print("{} logs".format(collection.count_documents({})))
        print("Methods:")
        for method in ["GET", "POST", "PUT", "PATCH","DELETE"]:
            count = collection.count_documents({"method": method})
            print("\tmethod {}: {}".format(method, count))
        status_count = collection.count_documents(
                {"method": "GET", "path": "/status"})
        print("{} status check".format(status_count))
