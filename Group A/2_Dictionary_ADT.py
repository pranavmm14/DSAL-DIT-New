"""
SPPU Computer Engineering DSA Lab 
Group A - 2

Implement all the functions of a dictionary (ADT) using hashing and handle collisions
using chaining with/without replacement. 
Data: Set of (key, value) pairs, Keys are mapped to values, Keys must be comparable, 
Keys must be unique. Standard Operations: Insert(key, value), Find(key), Delete(key).
"""

class Dictionary:

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def insert(self, key, value):
        hash_value = hash(key)
        print(hash_value)
        index = hash_value % self.capacity
        self.table[index].append((key, value))

    def find(self, key):
        hash_value = hash(key)
        index = hash_value % self.capacity
        for (k, v) in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_value = hash(key)
        index = hash_value % self.capacity
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return


dictionary = Dictionary(10)

dictionary.insert("1", "red")
dictionary.insert("2", "yellow")
dictionary.insert("3", "green")
dictionary.insert("4", "blue")

print(dictionary.find("2"))

dictionary.delete("2")

print(dictionary.find("2"))
