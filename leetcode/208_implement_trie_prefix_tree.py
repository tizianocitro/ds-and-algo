# !code: 208 !difficulty: medium, !from: https://leetcode.com/problems/implement-trie-prefix-tree, https://neetcode.io/problems/implement-prefix-tree

'''Problem:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Input:
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: [null, null, true, false, true, null, true]
Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith
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

class Trie:
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
