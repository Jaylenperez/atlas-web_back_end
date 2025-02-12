#!/usr/bin/env python3
import redis
import uuid
from typing import Union

class Cache:
    """Cache class to inherit with Redis."""

    def __init__(self):
        """Initialize Redis connection and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly genereated key.
        
        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.
            
        Returns:
            str: They key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key