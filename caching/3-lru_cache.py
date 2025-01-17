#!/usr/bin/env python3
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
        """
        Initializes the LRUCache instance.

        Sets up the cache with an OrderedDict to maintain
        the insertion order of items. Calls the parent class
        constructor to initialize the cache_data attribute
        from BaseCaching.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns item to the cache for the given key.

        If the cache size exceeds MAX_ITEMS, the least recently used item
        is discarded. The item is marked as the most recently used by moving
        it to the end of the ordered dictionary.

        Args:
            key (str): The key associated with the item to be stored.
            item (str): The value to store in the cache.

        If either key or item is None, the method does nothing.

        If the cache exceeds the MAX_ITEMS limit, the least recently used
        item is discarded, and a message is printed showing the key of
        the discarded item.
        """
        if key is None or item is None:
            return

        # If the item already exists in the cache, move it to the end
        # to mark it as recently used.
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        # If the cache size exceeds the limit, discard the least
        # recently used item.
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Returns the value associated with the given key.

        If the key exists in the cache, the item is returned and marked as
        recently used by moving it to the end of the ordered dictionary.

        Args:
            key (str): The key to search for in the cache.

        Returns:
            str: The value associated with the given key, or None if the key
                 doesn't exist or is None.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used.
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
