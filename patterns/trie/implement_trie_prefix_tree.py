# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/implement-trie-prefix-tree-medium-1

'''Problem:
Design and implement a Trie (also known as a Prefix Tree).
A trie is a tree-like data structure that stores a dynamic set of strings,
and is particularly useful for searching for words with a given prefix.

Implement the Solution class:
- Solution() initializes the object.
- void insert(word) inserts word into the trie, making it available for future searches.
- bool search(word) checks if the word exists in the trie.
- bool startsWith(prefix) checks if any word in the trie starts with the given prefix.

The word and prefix parsmeters consist only of lowercase English letters.

Input:
    Trie operations: ["Trie", "insert", "search", "startsWith"]
    Arguments: [[], ["apple"], ["apple"], ["app"]]
Output: [-1, -1, 1, 1]
Explanation: After inserting "apple", "apple" exists in the Trie. There is also a word that starts with "app", which is "apple".

Input:
    Trie operations: ["Trie", "insert", "search", "startsWith", "search"]
    Arguments: [[], ["banana"], ["apple"], ["ban"], ["banana"]]
Output: [-1, -1, 0, 1, 1]
Explanation: After inserting "banana", "apple" does not exist in the Trie but a word that starts with "ban", which is "banana", does exist.

Input:
    Trie operations: ["Trie", "insert", "search", "search", "startsWith"]
    Arguments: [[], ["grape"], ["grape"], ["grap"], ["gr"]]
Output: [-1, -1, 1, 1, 1]
Explanation: After inserting "grape", "grape" exists in the Trie. There are words that start with "grap" and "gr", which is "grape".
'''

# solution one
# Complexity:
# Time:
# - insert: O(n) where n is the length of the word
# - search: O(n) where n is the length of the word
# - startsWith: O(n) where n is the length of the prefix
# Space (whole trie):
# O(nm) - where n is the number of inserted words and m is the average word length
class TrieNode:
    def __init__(self):
        # dictionary to store child nodes
        self.children = {}
        # flag to represent end of a word
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    # inserts a word into the trie
    # O(n) time - where n is the length of the word
    # O(n) space - where n is the length of the word
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # returns if the word is in the trie
    # O(n) time - where n is the length of the word
    # O(1) space
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    # returns if there is any word in the trie that starts with the given prefix
    # O(n) time - where n is the length of the prefix
    # O(1) space
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True