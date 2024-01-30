#!/usr/bin/python3
"""Implementation class of basic cache.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Implementaion class of basic cache.

    Attributes:
        MAX_ITEMS: number of items that can be store in the cache
    """
    def put(self, key, item):
        """ Addition of item in cache.
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Item by key gettingg.
        """
        return self.cache_data.get(key, None)
