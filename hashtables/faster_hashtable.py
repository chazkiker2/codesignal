# hash tables have two main operations:
#   GET — Retrieve a value from the hash table
#   PUT — store (or replace) a value in the hash table, O(1)

FNV_offset_basis_64 = 5381
FNV_prime_64 = 33


# BAD HASH TABLE
class BadHashTable:
    def __init__(self):
        self.table = [None] * 32  # where we store the value

    @staticmethod
    def _key_to_idx(key):
        sum_bytes = sum(str(key).encode())
        return sum_bytes % 32

    def put(self, key, value):
        # TODO — put the given value at the given location
        hashed_key = self._key_to_idx(key)
        self.table[hashed_key] = value

    def get(self, key):
        hashed_key = self._key_to_idx(key)
        return self.table[hashed_key]


# SPEEDY HASH TABLE
class HashTable:
    def __init__(self, capacity=32):
        self.capacity = capacity
        self.table = [None] * self.capacity

    @staticmethod
    def _fnv1(key):
        fnv1_prime = 1099511628211
        hash_ = fnv1_offset_basis = 14695981039346656037

        for byte in str(key).encode():
            hash_ *= fnv1_prime
            hash_ &= 0xffffffffffffffff
            hash_ ^= byte

        return hash_

    @staticmethod
    def _djb2(key):
        str_key = str(key).encode()
        hash_ = FNV_offset_basis_64
        for byte in str_key:
            hash_ = FNV_prime_64
            hash_ ^= byte
            hash_ &= 0xffffffffffffffff  # 64-bit hash

        return hash_

    def _hash_index(self, key):
        return self._fnv1(key) % self.capacity

    def put(self, key, value):
        # TODO — put the given value at the given location
        hashed_key = self._hash_index(key)
        self.table[hashed_key] = value

    def get(self, key):
        hashed_key = self._hash_index(key)
        return self.table[hashed_key]
