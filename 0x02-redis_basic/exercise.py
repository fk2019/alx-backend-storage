#!/usr/bin/env python3
"""Example of redis cache"""
from functools import wraps
from typing import Union, Callable, Optional
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """decorator function to define a wrapper function
    that counts times Cache class methods are called"""
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(name)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator func stores history of inputs and outputs for method"""
    name = method.__qualname__
    inputs = name + ':inputs'
    outputs = name + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper method"""
        self._redis.rpush(inputs, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(res))
        return res
    return wrapper


def replay(method: Callable) -> None:
    """Display history of calls of particular function"""
    name = method.__qualname__
    inputs = name + ':inputs'
    outputs = name + ':outputs'
    redis = method.__self__._redis
    count = redis.get(name).decode('utf-8')
    print('{} was called {} times:'.format(name, count))
    zipped = zip(redis.lrange(inputs, 0, -1), redis.lrange(outputs, 0, -1))
    for i, o in list(zipped):
        i = i.decode('utf-8')
        o = o.decode('utf-8')
        print('{}(*{}) -> {}'.format(name, i, o))


class Cache():
    """Class Cache generates randon key and returns it"""
    def __init__(self):
        """Cache class for caching"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key amd store input in Redis"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """Receives key and optional func that returns desired data"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """Get data as string"""
        return data.decode('utf-8')

    def get_int(self, data: str) -> int:
        """Get data as int"""
        return int(data)
