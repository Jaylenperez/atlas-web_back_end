#!/usr/bin/env python3
"""FIFO Caching System"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching System

    Implements a caching system using the FIFO (First-In-First-Out) algorithm.
    """

    def __init__(self):
        """Initialize the FIFO cache"""
        super().__init__()
        self.queue = []  # Track the order of inserted keys

    def put(self, key, item):
        """Add an item to the cache using FIFO

        Args:
            key (str): The key of the item to add.
            item (any): The value of the item to add.
        """
        if key is None or item is None:
            return

        # If the key already exists, remove it from the queue
        if key in self.cache_data:
            self.queue.remove(key)

        # Add the item to the cache and the queue
        self.cache_data[key] = item
        self.queue.append(key)

        # If cache exceeds MAX_ITEMS, remove the oldest item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.pop(0)  # Remove the first key in the queue
            del self.cache_data[oldest_key]  # Remove it from the cache
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve an item by key

        Args:
            key (str): The key to look up in the cache.

        Returns:
            any: The value associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
