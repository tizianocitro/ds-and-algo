# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/group-anagrams-medium

'''Problem:
Given a list of strings, the task is to group the anagrams together.
An anagram is a word or phrase formed by rearranging the letters of another, such as "cinema", formed from "iceman".

Input: ["dog", "god", "hello"]
Output: [["dog", "god"], ["hello"]]
Explanation: "dog" and "god" are anagrams, so they are grouped together. "hello" does not have any anagrams in the list, so it is in its own group.

Input: ["listen", "silent", "enlist"]
Output: [["listen", "silent", "enlist"]]
Explanation: All three words are anagrams of each other, so they are grouped together.

Input: ["abc", "cab", "bca", "xyz", "zxy"]
Output: [["abc", "cab", "bca"], ["xyz", "zxy"]]
Explanation: "abc", "cab", and "bca" are anagrams, as are "xyz" and "zxy".
'''

# solution one using character frequency to encode the words
# Complexity:
# O(nk) time - where n is the number of words and k is the length of the longest word
# O(nk) space - to store the encoded words, k for the keys and n for the values
class Solution:
    def groupAnagrams(self, strs):
        # holds encoded words as key and list of words as value
        anagrams = {}

        for s in strs:
            # get the string as a tuple of character frequencies
            encoded_s = self.getFrequencyEncodedString(s)
            if encoded_s not in anagrams:
                anagrams[encoded_s] = []

            # add the original word to the list of values for the encoded word key
            anagrams[encoded_s].append(s)

        return anagrams.values()

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

# solution two using sorting to encode the words
# Complexity:
# O(nklogk) time - where n is the number of words and k is the length of the longest word
# O(nk) space - to store the sorted words, k for the keys and n for the values
class Solution:
    def groupAnagrams(self, strs):
        # holds sorted words as key and list of words as value
        anagrams = {}

        for s in strs:
            # encode the string to its sorted version
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            # add the original word to the list of values for the sorted word key
            anagrams[sorted_s].append(s)

        # the values of the dictionary are the groups
        return anagrams.values()