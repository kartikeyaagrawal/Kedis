import time

class TTLCache:
    def __init__(self):
        """
        Initialize the TTLCache with no default TTL.
        """
        self.cache = {}

    def _is_expired(self, key):
        """
        Check if the cache entry for the given key is expired.

        :param key: The cache key to check.
        :return: True if the entry is expired, False otherwise.
        """
        if key in self.cache:
            entry = self.cache[key]
            if entry['expires_at'] is None:
                # Infinite TTL
                return False
            return time.time() > entry['expires_at']
        return True

    def add(self, key, value, ttl=None):
        """
        Add a new key-value pair to the cache with an optional TTL.

        :param key: The key for the cache entry.
        :param value: The value to cache.
        :param ttl: Time-to-live for the cache entry in seconds. Use None for infinite TTL.
        """
        ttl = int(ttl)
        self.cache[key] = {
            'value': value,
            'expires_at': time.time() + ttl if ttl is not None else None
        }

    def get(self, key):
        """
        Get the value associated with a key from the cache.

        :param key: The key to retrieve.
        :return: The cached value, or None if the key is not found or expired.
        """
        
        if key in self.cache:
            if not self._is_expired(key):
                return self.cache[key]['value']
            else:
                # Remove expired entry
                self.remove(key)
        return None

    def set(self, key, value, ttl=None):
        """
        Update the value of an existing cache entry with an optional TTL.

        :param key: The key for the cache entry.
        :param value: The new value to cache.
        :param ttl: Time-to-live for the cache entry in seconds. Use None for infinite TTL.
        """
        ttl = int(ttl)
        if key in self.cache:
            if not self._is_expired(key):
                self.cache[key]['value'] = value
                self.cache[key]['expires_at'] = time.time() + ttl if ttl is not None else None
            else:
                # Re-add if expired
                self.add(key, value, ttl)
        else:
            self.add(key, value, ttl)

    def remove(self, key):
        """
        Remove a key-value pair from the cache.

        :param key: The key to remove.
        """
        if key in self.cache:
            del self.cache[key]

    def __str__(self):
        """
        Display the cache content for debugging purposes.
        """
        return str({k: v['value'] for k, v in self.cache.items() if not self._is_expired(k)})


# # Example Usage
# cache = TTLCache()

# # Adding values with specific TTL
# cache.add('key1', 'value1', ttl=10)  # Expires in 10 seconds
# cache.add('key2', 'value2', ttl=None)  # Infinite TTL

# # Getting values
# print(cache.get('key1'))  # Outputs: value1
# print(cache.get('key2'))  # Outputs: value2

# # Updating values
# cache.set('key1', 'new_value1', ttl=5)  # Update value and TTL to 5 seconds
# print(cache.get('key1'))  # Outputs: new_value1

# # Removing values
# cache.remove('key2')
# print(cache.get('key2'))  # Outputs: None (since it has been removed)

# # Cache entry with infinite TTL will not expire
# time.sleep(15)
# print(cache.get('key2'))  # Outputs: None (since it was removed)
# print(cache.get('key1'))  # Outputs: None (since TTL expired)
