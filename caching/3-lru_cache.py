#!/usr/bin/env python3
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching
    Implements the LRU caching algorithm
    """

    def __init__(self):
        """Initializes the LRUCache instance"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns item to the dictionary for the given key.
        If the cache size exceeds MAX_ITEMS, discard the LRU item.
        """
        if key is None or item is None:
            return

        # If the cache is full, remove the oldest item (least recently used)
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Returns the value associated with the given key,
        or None if key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
