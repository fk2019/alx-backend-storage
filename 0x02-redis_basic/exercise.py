#!/usr/bin/en python3
"""Example of redis cache"""
from typing import Union
import redis
import uuid


class Cache():
    """Class Cache generates randon key and returns it"""
    def __init__(self):
        """Cache class for caching"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key amd store input in Redis"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
