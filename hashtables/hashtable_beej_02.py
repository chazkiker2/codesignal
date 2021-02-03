# class HashNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# # SPEEDY HASH TABLE
# class HashTable:
#     def __init__(self, capacity=32):
#         self.capacity = capacity
#         # self.table = [None] * self.capacity
#         self.table = [[] for _ in range(self.capacity)]
#
#     @staticmethod
#     def _fnv1(key):
#         fnv1_prime = 1099511628211
#         hash_ = fnv1_offset_basis = 14695981039346656037
#
#         for byte in str(key).encode():
#             hash_ *= fnv1_prime
#             hash_ &= 0xffffffffffffffff
#             hash_ ^= byte
#
#         return hash_
#
#     @staticmethod
#     def _djb2(key):
#         str_key = str(key).encode()
#         hash_ = FNV_offset_basis_64
#         for byte in str_key:
#             hash_ = FNV_prime_64
#             hash_ ^= byte
#             hash_ &= 0xffffffffffffffff  # 64-bit hash
#
#         return hash_
#
#     def _hash_index(self, key):
#         return self._fnv1(key) % self.capacity
#
#     def put(self, key, value):
#         # TODO — put the given value at the given location
#         hashed_key = self._hash_index(key)
#         self.table[hashed_key] = value
#
#     def get(self, key):
#         hashed_key = self._hash_index(key)
#         entries = self.table[hashed_key]

# ht = HashTable()
# print(ht.table)
# ht.table[1].append(4)
# print(ht.table)
