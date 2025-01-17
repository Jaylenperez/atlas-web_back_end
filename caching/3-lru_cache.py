#!/usr/bin/env python3
"""
LRUCache module.

This module implements an LRU (Least Recently Used) cache system.
It inherits from the BaseCaching class and implements the LRU algorithm
for managing cache items. If the cache exceeds a predefined limit (MAX_ITEMS),
the least recently used item will be discarded to make space for new items.

The LRUCache class uses an OrderedDict to maintain the order of items based
on their usage. The most recently used items are at the end of the dictionary,
and the least recently used items are at the start.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching.

    Implements an LRU (Least Recently Used) caching algorithm. The class
    manages a cache that stores a limited number of items. If the cache
    exceeds the predefined limit (MAX_ITEMS), the least recently used
    item is discarded to make space for new items.

    Attributes:
        cache_data (OrderedDict): An ordered dictionary that stores the cache
                                   items in the order they were last accessed.
    """

    def __init__(self):
        """Initializes the LRUCache instance."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns item to the cache for the given key."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Returns the value associated with the given key."""
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
