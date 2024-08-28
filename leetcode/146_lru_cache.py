# !code: 146, !difficulty: medium, !from: https://leetcode.com/problems/lru-cache/

'''Problem:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache (https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU).

Implement the LRUCache class:
- LRUCache(int capacity): initialize the LRU cache with positive size capacity.
- int get(int key): return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value): update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
  If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Input:
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation:
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1);    // return -1 (not found)
    lRUCache.get(3);    // return 3
    lRUCache.get(4);    // return 4
'''

# solution one using hash map and doubly linked list
# Complexity:
# O(1) time - for both get and put
# O(n) space - where n is the capacity of the cache (for the hash map and doubly linked list)
class Node:

    # -1 is the default value for key and value,
    # and it is used for the head and tail nodes
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # how many elements the cache can hold
        self.capacity = capacity
        # key -> node mapping
        self.cache = {}

        # head and tail will always be dummy node to simplify edge cases
        # in this way, lru = self.head.next and mru = self.tail.prev
        self.head, self.tail = Node(), Node()
        # initially the head and tail are connected
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        # when we retrieve a new node, we want to make it the most recently used
        # by putting it as the previous node of the tail, so we remove it from
        # its current position and append it as the prev of the tail
        node = self.cache[key]
        self.remove(node)
        self.append(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if key is into the cache, we remove it from its current position
        # so that it can be appended as the prev of the tail and be the most recently used
        # because it should be as if it was just added and a new element
        # should no be considered as the least recently used
        if key in self.cache:
            self.remove(self.cache[key])

        # create a new node and add it to the cache by adding
        # it to both the hash map and the doubly linked list
        node = Node(key, value)
        self.cache[key] = node
        self.append(node)

        # if we exceed the capacity, we remove the least recently used
        # which will always the successor of the head, so we
        # remove it from both the cache and the doubly linked list
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node):
        """
        Remove a node from the doubly linked list
        """
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def append(self, node):
        """
        append a node to the end of the doubly linked list
        as the predecessor of the tail
        """
        prev, next = self.tail.prev, self.tail
        # set the prev of the tail as the node prev
        node.prev = prev
        # set the tail as the next of the node
        node.next = next
        # the prev of the tail now needs to have the node as the prev
        prev.next = node
        # prev of the tail now should be the new node
        next.prev = node

# The LRUCache object will be instantiated and called as such:
# cache = LRUCache(capacity)
# cache.put(key, value)
# value = cache.get(key)