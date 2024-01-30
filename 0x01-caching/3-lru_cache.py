#!/usr/bin/python3
"""Implementation Class of LRU Cache.
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Implementation Class of LRU Cache.

    Attributes:
        __keys (list): Storing cache keys from least to most accessed.
        __rlock (RLock): locks accessed resources; preventing race conditionn.
    """
    def __init__(self):
        """ Instantiation method; setting instance attributes.
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """Additon of item in cache.
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """ Getging item by keyy.
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__keys:
                self._balance(key)
        return value

    def _balance(self, keyIn):
        """ Removing earliest item from cache at MAX size.
        """
        keyOut = None
        with self.__rlock:
            keysLength = len(self.__keys)
            if keyIn not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = self.__keys.pop(0)
                    self.cache_data.pop(keyOut)
            else:
                self.__keys.remove(keyIn)
            self.__keys.insert(keysLength, keyIn)
        return keyOut
