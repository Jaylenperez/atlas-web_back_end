#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional
import functools

def count_calls(method: Callable) -> Callable:
        """
        Decorator that counts the number of calls made to a method and stores it in Redis.
        
        Args:
            method (Callable): The method to decorate.
        
        Returns:
            Callable: The wrapped method that increments the call count.
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            """Increment the call count for the method in Redis."""
            key = method.__qualname__  # Use the qualified name of the method as the Redis key
            self._redis.incr(key)  # Increment the call count for the method
            return method(self, *args, **kwargs)  # Call the original method and return its result
        return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a method in Redis.
    
    Args:
        method (Callable): The method to decorate.
    
    Returns:
        Callable: The wrapped method that stores input/output history.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Store input arguments and output results in Redis."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))
        
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        
        return output
    return wrapper

class Cache:
    """Cache class to inherit with Redis."""

    def __init__(self):
        """Initialize Redis connection and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
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
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, bytes, None]:
        """
        Retrieve data from Redis and apply an optional transformation function.
        
        Args:
            key (str): The key to retrieve the data from Redis.
            fn (Optional[Callable]): A function to transform the data.
        
        Returns:
            Union[str, int, bytes, None]: The retrieved data after transformation, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data from Redis and decode it as a UTF-8 string."""
        data = self.get(key)
        if data is None:
            return None
        return data.decode("utf-8")

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data from Redis and convert it to an integer."""
        data = self.get(key)
        if data is None:
            return None
        return int(data)
    

    def replay(cache: 'Cache', method: Callable):
        """
        Display the history of calls of a decorated method.

        Args:
            cache (Cache): The Cache instance to retrieve history from.
            method (Callable): The decorated method to replay.
        """
        redis_instance = cache._redis  # Access Redis instance
        method_name = method.__qualname__  # Get the qualified name of the method

        inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
        outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)

        print(f"{method_name} was called {len(inputs)} times:")

        for input_args, output in zip(inputs, outputs):
            input_str = input_args.decode("utf-8")
            output_str = output.decode("utf-8") if output else "None"
            print(f"{method_name}(*{input_str}) -> {output_str}")
