# !code: 14, !difficulty: easy, !from: https://leetcode.com/problems/longest-common-prefix/

'''Problem:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

# solution one using vertical scanning
# Complexity:
# O(nm) time, where n is the number of words and m is the length of the longest word
# O(1) space
class Solution:
    def longestCommonPrefix(self, strs: str) -> str:
        # for each column in the matrix of words
        for i in range(len(strs[0])):
            # take the character of the first word in the list at the current column i
            ch = strs[0][i]
            # for each word in the list starting from the second word
            for j in range(1, len(strs)):
                # if we reach the end of a word or the character at the current column i
                # is not the same as the character of the first word at the current column i
                if i == len(strs[j]) or strs[j][i] != ch:
                    # return the prefix from the first word up to the current column i
                    # because that is the longest common prefix
                    return strs[0][0:i]

        # otherwise they are all the same, so return the first word
        return strs[0]

# solution two using trie
# Complexity:
# O(nm) time, where n is the number of words and m is the length of the longest word
# O(nm) space, where n is the number of words and m is the length of the longest word
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        # this is used to check if the node has more than one child
        self.children_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                # when you add a new child to a node,
                # increment the count of its children
                node.children_count += 1
            node = node.children[ch]
        node.is_end = True

    def longest_prefix(self):
        longest = 0
        node = self.root
        # while nodes have only one children, then they are part of the prefix
        while node.children_count == 1:
            longest += 1
            # this will always contain 1 key because of the while condition
            for ch in node.children.keys():
                node = node.children[ch]
            # if we reach the end of a word, then we can return the longest prefix
            # because that word will be the longest common prefix
            if node.is_end:
                return longest
        return longest

class Solution:
    def longestCommonPrefix(self, strs: str) -> str:
        trie = Trie()

        # add each word to the trie
        for w in strs:
            # if a word is empty, then there is no common prefix
            if not w:
                return ''
            trie.add(w)

        # find the end of the longest common prefix
        end = trie.longest_prefix()

        # return the longest common prefix by taking it from any word in the list
        return strs[0][0:end]
