# !code: 49, !difficulty: medium, !from: https://leetcode.com/problems/group-anagrams/

'''Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Constraints:
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
'''

# solution one using character frequency to encode the words
# Complexity:
# O(nk) time - where n is the number of words and k is the length of the longest word
# O(nk) space - to store the encoded words, k for the keys and n for the values
class Solution:
    def groupAnagrams(self, strs):
        # holds encoded words as key and list of words as value
        groups = {}

        for s in strs:
            # get the string as a tuple of character frequencies
            encoded_s = self.getFrequencyEncodedString(s)
            if encoded_s not in groups:
                groups[encoded_s] = []

            # add the original word to the list of values for the encoded word key
            groups[encoded_s].append(s)

        return groups.values()

    # returns a tuple containing the frequency of each character in the string
    # e.g., 'abc' -> (1, 1, 1, 0, 0, 0, ..., 0)
    # e.g., 'aab' -> (2, 1, 0, 0, 0, 0, ..., 0)
    # e.g., 'azzz' -> (1, 0, 0, ..., 0, 3)
    def getFrequencyEncodedString(self, s):
        # 26 because we are considering only lowercase english letters
        encoded = [0] * 26
        for ch in s:
            ch_ix = ord(ch) - ord('a')
            encoded[ch_ix] += 1

        # retuns a tuple because it can be used as a key in a dictionary
        return tuple(encoded)

# solution two identical to solution one but using defaultdict
# Complexity:
# O(nk) time - where n is the number of words and k is the length of the longest word
# O(nk) space - to store the encoded words, k for the keys and n for the values
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # holds encoded words as key and list of words as value
        # with defaultdict, we don't need to check if the key exists before adding a value
        groups = defaultdict(list)

        for s in strs:
            # get the string as a tuple of character frequencies
            encoded_s = self.getFrequencyEncodedString(s)

            # add the original word to the list of values for the encoded word key
            groups[encoded_s].append(s)

        return groups.values()

    # returns a tuple containing the frequency of each character in the string
    # e.g., 'abc' -> (1, 1, 1, 0, 0, 0, ..., 0)
    # e.g., 'aab' -> (2, 1, 0, 0, 0, 0, ..., 0)
    # e.g., 'azzz' -> (1, 0, 0, ..., 0, 3)
    def getFrequencyEncodedString(self, s):
        # 26 because we are considering only lowercase english letters
        encoded = [0] * 26
        for ch in s:
            # it is also possible to do:
            # ch_ix = ord(ch) % 26
            ch_ix = ord(ch) - ord('a')
            encoded[ch_ix] += 1

        # retuns a tuple because it can be used as a key in a dictionary
        return tuple(encoded)

# solution three using sorting to encode the words
# Complexity:
# O(nklogk) time - where n is the number of words and k is the length of the longest word
# O(nk) space - to store the sorted words, k for the keys and n for the values
class Solution:
    def groupAnagrams(self, strs):
        # holds sorted words as key and list of words as value
        groups = {}

        for s in strs:
            # encode the string to its sorted version
            sorted_s = ''.join(sorted(s))
            if sorted_s not in groups:
                groups[sorted_s] = []

            # add the original word to the list of values for the sorted word key
            groups[sorted_s].append(s)

        # the values of the dictionary are the groups
        return groups.values()
