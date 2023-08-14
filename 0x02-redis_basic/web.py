#!/usr/bin/env python3
"""Implementing an expiry web cache and tracker
"""
from functools import wraps
from typing import Callable
import redis
import requests

redis = redis.Redis()


def count(method: Callable) -> Callable:
    """Decorator to count times url is accessed"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        url = args[0]
        redis.incr('count:{}'.format(url))
        cache = redis.get('{}'.format(url))
        if cache:
            return cache.decode('utf-8')
        redis.setex(url, 10, method(url))
        return method(*args, **kwargs)
    return wrapper


@count
def get_page(url: str) -> str:
    """Use requests module to obtain HTML content of
    url and return it"""
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
