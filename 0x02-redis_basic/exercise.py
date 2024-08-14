#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache classe for interacting with redis."""
    def __init__(self) -> None:
        """init cache instance:
        init new redis client and flush redis db.
        ps: redis client stored as private variable.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis with a random key(string)
        as a key = value.
        return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
