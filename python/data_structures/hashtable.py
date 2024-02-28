class Hashtable:
    """
    Hashtable implementation using chaining for collision resolution.
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = [[] for _ in range(size)]

    def hash(self, key):
        """
        Generate a hash for a given key.
        """
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        """
        Set the key and value in the hashtable.
        """
        index = self.hash(key)
        bucket = self._buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        """
        Return the value associated with the key in the hashtable.
        """
        index = self.hash(key)
        bucket = self._buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def has(self, key):
        """
        Check if the key exists in the hashtable.
        """
        index = self.hash(key)
        bucket = self._buckets[index]
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def keys(self):
        """
        Return a collection of keys in the hashtable.
        """
        keys_list = []
        for bucket in self._buckets:
            keys_list.extend([k for k, _ in bucket])
        return keys_list

    def display(self):
        """
        Utility method to display hashtable contents (for debugging and testing).
        """
        return [bucket for bucket in self._buckets if bucket]

