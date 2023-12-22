from collections import defaultdict

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = defaultdict(list)
    def hash(self, key):
        return key % self.size
    def get(self, key):
        return self.table[self.hash(key)]
    def put(self, key, value):
        self.table[self.hash(key)].append(value)
