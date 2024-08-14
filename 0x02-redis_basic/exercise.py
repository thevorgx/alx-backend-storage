#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """get key"""
        get_key = self._redis.get(key)
        if get_key is None:
            return(None)
        if fn:
            return (fn(get_key))
        return (get_key)

    def get_str(self, key: str) -> str:
        """get key as str"""
        key_to_convert = self.get(key, str)
        return(key_to_convert)

    def get_int(self, key: int) -> int:
        """get key as int"""
        key_to_convert = self.get(key, int)
        return (key_to_convert)
