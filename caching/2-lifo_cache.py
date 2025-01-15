#!/usr/bin/env python3
""" LIFO Caching Module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching system """

    def __init__(self):
        """ Initialize class instance """
        super().__init__()
        self.stack = []  # To track the insertion order for LIFO

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # Add or update the cache
        if key in self.cache_data:
            self.stack.remove(key)
        self.cache_data[key] = item
        self.stack.append(key)

        # Check if the cache exceeds the limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)  # Discard the second-last key
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
