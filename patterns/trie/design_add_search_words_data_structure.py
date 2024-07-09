# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/design-add-and-search-words-data-structure-medium-1

'''Problem:
Design a data structure that supports the addition of new words and the ability to check if a string matches any previously added word.

Implement the Solution class:
- Solution(): initializes the object.s
- void addWord(word): inserts word into the data structure, making it available for future searches.
- bool search(word): checks if there is any word in the data structure that matches word.
  The method returns true if such a match exists, otherwise returns false.

The word parameter in addWord consists of lowercase English letters.
The word parameter in search consist of '.' or lowercase English letters.

Note: In the search query word, the character '.' can represent any single letter,
effectively serving as a wildcard character.

Input:
    ["Solution", "addWord", "addWord", "search", "search"]
    [[], ["apple"], ["banana"], ["apple"], ["....."]]
Output: [-1, -1, -1, 1, 1]
Explanation: After adding the words "apple" and "banana", searching for "apple" will return true since "apple" is in the data structure. Searching for "....." will also return true as both "apple" and "banana" match the pattern.

Input:
    ["Solution", "addWord", "addWord", "search", "search"]
    [[], ["cat"], ["dog"], ["c.t"], ["d..g"]]
Output: [-1, -1, -1, 1, 0]
Explanation: "c.t" matches "cat" and "d..g" doesn't matches "dog".

Input:
    ["Solution", "addWord", "search", "search"]
    [[], ["hello"], ["h.llo"], ["h...o"]]
Output: [-1, -1, 1, 0]
Explanation: "h.llo" and "h...o" both match "hello".
'''

# solution one
# Complexity:
# Time:
# - addWord: O(n) where n is the length of the word
# - search: O(nm) time - where n is the length of the word and m is the
# number of children of a node, this happens when the word has wildcard characters
# Space (whole trie):
# O(nm) - where n is the number of inserted words and m is the average word length
class TrieNode:
    def __init__(self):
        # initialize children as a dictionary to represent all possible next characters
        self.children = {}  
        # flag to check if the current node marks the end of any word
        self.is_end = False  

class Solution:
    def __init__(self):
        self.root = TrieNode()

    # O(n) time - where n is the length of the word
    # O(n) space - where n is the length of the word
    def addWord(self, word: str):
        node = self.root
        # if current character isn't already a child of the node, add it
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # print the char associated with each child of a node
            # print([child for child in node.children.keys()])
            # move on to the next character/node
            node = node.children[ch]
        # after processing all characters of the word,
        # mark the current node as end of a word            
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._search(self.root, 0, word)

    # O(nm) time - where n is the length of the word and m is the number of children of a node
    # this happens when the word has wildcard characters
    # O(n) space - where n is the length of the word,
    # because we won't have more than n recursive calls on the call stack
    def _search(self, node, current_index, word):
        # if we have reached the end of the word, check
        # if the current node marks the end of a word in the trie
        if current_index == len(word):
            return node.is_end

        current_ch = word[current_index]

        # check for wildcard character
        if current_ch == '.':
            # recursively search for all possible characters in place of the wildcard
            # if any node returns True, then it means the word exists in the trie
            return any(
                self._search(child, current_index + 1, word) for child in node.children.values()
            )

            # in alternative to the any() function, we can use a simple for loop
            # these two approaches are equivalent, the above is more concise
            # for child in node.children.values():
            #     if self._search(child, current_index + 1, word):
            #         return True

        # if the current character doesn't exist in children, word can't exist in the trie
        if current_ch not in node.children:
            return False

        # move to the next character/node and see if you can reach a word
        # that exists in the trie, starting from the current character
        return self._search(node.children[current_ch], current_index + 1, word)

# solution two
# Complexity:
# Time:
# - addWord: O(n) where n is the length of the word
# - search: O(nm) time - where n is the length of the word and m is the
# number of children of a node, this happens when the word has wildcard characters
# Space (whole trie):
# O(nm) - where n is the number of inserted words and m is the average word length
class TrieNode:
    def __init__(self):
        # initialize children as a dictionary to represent all possible next characters
        self.children = {}  
        # flag to check if the current node marks the end of any word
        self.is_end = False 

class Solution:
    def __init__(self):
        self.root = TrieNode()

    # O(n) time - where n is the length of the word
    # O(n) space - where n is the length of the word
    def addWord(self, word: str):
        node = self.root
        for ch in word:
            # if current character isn't already a child of the node, add it
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # move on to the next character/node
            node = node.children[ch]
        # after processing all characters of the word,
        # mark the current node as end of a word
        node.isEnd = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    # O(nm) time - where n is the length of the word and m is the number of children of a node
    # this happens when the word has wildcard characters
    # O(n) space - where n is the length of the word,
    # because we won't have more than n recursive calls on the call stack
    def _search(self, word: str, node: TrieNode) -> bool:
        for i, ch in enumerate(word):
            # check for wildcard character
            if ch == '.':
                # recursively search for all possible characters in place of the wildcard
                return any(
                    self._search(word[i + 1:], node.children[child]) for child in node.children if child
                )

                # in alternative to the any() function, we can use a simple for loop
                # these two approaches are equivalent, the above is more concise
                # for child in node.children.values():
                #     if self._search(word[i + 1:], child):
                #         return True

            # if character doesn't exist in children, word can't exist in the trie
            if ch not in node.children:
                return False

            # move to the next character/node.
            node = node.children[ch]

        # after processing all characters of the word, return if it's a valid word.
        return node.isEnd