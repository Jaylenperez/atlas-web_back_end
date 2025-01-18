#!/usr/bin/env python3
"""
MRUCache module.

This module implements an MRU (Most Recently Used) cache system.
It inherits from the BaseCaching class and implements the MRU algorithm
for managing cache items. If the cache exceeds a predefined limit (MAX_ITEMS),
the most recently used item will be discarded to make space for new items.

The MRUCache class uses a dictionary to maintain cache items. When the cache
exceeds the MAX_ITEMS limit, the most recently used item is removed.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching.

    Implements an MRU (Most Recently Used) caching algorithm. The class
    manages a cache that stores a limited number of items. If the cache
    exceeds the predefined limit (MAX_ITEMS), the most recently used
    item is discarded to make space for new items.

    Attributes:
        cache_data (OrderedDict): An ordered dictionary that stores
        the cache items.
    """

    def __init__(self):
        """
        Initializes the MRUCache instance.

        Sets up the cache using an OrderedDict (cache_data). The cache will
        store items and track the most recently used item when the cache
        exceeds the MAX_ITEMS limit.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds the item to the cache for the given key.

        If the cache size exceeds MAX_ITEMS, the most recently used item
        will be discarded. The item is marked as the most recently used by
        updating it in the dictionary.

        Args:
            key (str): The key associated with the item to be stored.
            item (str): The value to store in the cache.

        If either key or item is None, the method does nothing.

        If the cache exceeds the MAX_ITEMS limit, the most recently used
        item is discarded, and a message is printed showing the key of
        the discarded item.
        """
        if key is None or item is None:
            return

        # Update the cache with the new item, marking it as most recently used
        self.cache_data[key] = item

        #
