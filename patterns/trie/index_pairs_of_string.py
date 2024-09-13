# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/index-pairs-of-a-string-easy

'''Problem:
Given a string text and a list of strings words, identify all [i, j] index pairs such that the substring text[i...j] is in words.
These index pairs should be returned in ascending order, first by the start index, then by the end index.
Find every occurrence of each word within the text, ensuring that overlapping occurrences are also identified.

The text and words consist of lowercase English letters.
All the strings of words are unique.

Input: text = "bluebirdskyscraper", words = ["blue", "bird", "sky"]
Output: [[0, 3], [4, 7], [8, 10]]
Explanation: The word "blue" is found from index 0 to 3, "bird" from 4 to 7, and "sky" from 8 to 10 in the string.

Input: text = "programmingisfun", words = ["pro", "is", "fun", "gram"]
Output: [[0, 2], [3, 6], [11, 12], [13, 15]]
Explanation: "pro" is found from 0 to 2, "gram" from 3 to 6, "is" from 11 to 12, and "fun" from 13 to 15.

Input: text = "interstellar", words = ["stellar", "star", "inter"]
Output: [[0, 4], [5, 11]]
Explanation: "inter" is found from 0 to 4, and "stellar" from 5 to 11. "star" is not found.
'''

# solution one, less cleaner version of solution one
# Complexity:
# O(n * m + t^2) time - where n is the number of words,
# m is the average length of the words, and t is the length of the text
# O(n * m) space - to store the trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # inserts a word into the trie
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

class Solution:
    def indexPairs(self, text, words):
        trie = Trie()

        # populate the trie with the list of words
        # this block has complexity O(n * m) where n is the
        # number of words and m is the average length of these words
        for word in words:
            trie.insert(word)

        result = []
        # this block has complexity O(t^2) where t is the length of the text
        # for each starting position for a substring
        # iterating this way from smaller to larger index ensures the order
        for start in range(len(text)):
            node = trie.root
            for end in range(start, len(text)):
                ch = text[end]
                # break if the character is not in the trie,
                # meaning the current substring is not one of
                # the input words that are in the trie
                if ch not in node.children:
                    break
                node = node.children[ch]
                # if the end of the substring is a word in the trie
                # add the index pair to the result list
                if node.isEnd:
                    # add index pair if a word is found
                    result.append([start, end])

        # return a list of lists containing index pairs
        return result

# solution two, less cleaner version of solution one
# Complexity:
# O(n * m + t^2) time - where n is the number of words,
# m is the average length of the words, and t is the length of the text
# O(n * m) space - to store the trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def indexPairs(self, text, words):
        root = TrieNode()

        # populate the trie with the list of words
        # for each word, follow the insert pattern for a trie
        # in this way, we add all the words to the trie
        # this block has complexity O(n * m) where n is the
        # number of words and m is the average length of these words
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        result = []
        # this block has complexity O(t^2) where t is the length of the text
        # for each starting position for a substring
        # iterating this way from smaller to larger index ensures the order
        for start in range(len(text)):
            node = root
            # for each ending position for a substring starting at index start
            for end in range(start, len(text)):
                ch = text[end]
                # break if the character is not in the trie,
                # meaning the current substring is not one of
                # the input words that are in the trie
                if ch not in node.children:
                    break
                node = node.children[ch]
                # if the end of the substring is a word in the trie
                # add the index pair to the result list
                if node.is_end:
                    # add index pair if a word is found
                    result.append([start, end])

        # return a list of lists containing index pairs
        return result
