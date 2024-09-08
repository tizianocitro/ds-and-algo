# !difficulty: medium, !from: 

'''Problem:
Given a string s and an array of words dictionary. Break the string s into multiple
non-overlapping substrings such that each substring should be part of the words.
There are some characters left which are not part of any substring.

Return the minimum number of remaining characters in s, which are not part of any substring after string break-up.

consider that:
- dictionary[i] and s consists of only lowercase English letters
- dictionary contains distinct words

Input: s = "amazingracecar", words = ["race", "car"]
Output: 7
Explanation: The string s can be rearranged to form "racecar", leaving 'a', 'm', 'a', 'z', 'i', 'n', 'g' as extra.

Input: s = "bookkeeperreading", words = ["keep", "read"]
Output: 9
Explanation: The words "keep" and "read" can be formed from s, but 'b', 'o', 'o', 'k', 'e', 'r', 'i', 'n', 'g' are extra.

Input: s = "thedogbarksatnight", words = ["dog", "bark", "night"]
Output: 6
Explanation: The words "dog", "bark", and "night" can be formed, leaving 't', 'h', 'e', 's', 'a', 't' as extra characters.
'''

# solution one using a trie and a counter
# Complexity:
# O(nm + s^2) time - where n is the number of words in the dictionary and m is the average length of the words in the dictionary
# and s is the length of the string s because we have to iterate over all the characters of the string in case it doesn't contain any word from the dictionary
# O(nm) space - to store the words in the trie
class TrieNode:
    def __init__(self):
        # representing each character of the alphabet
        self.children = [None] * 26
        # to determine if the current TrieNode marks the end of a word
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # get the index of the character in the alphabet
    def chartToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        node = self.root
        for ch in word:
            ix = self.chartToIndex(ch)
            if not node.children[ix]:
                node.children[ix] = TrieNode()
            # print the char associated to each child of the node
            # print([chr(ord('a') + i) for i in range(len(node.children)) if node.children[i]])
            node = node.children[ix]
        node.is_end = True

    # check if the word contains starting from the start index
    # a word from the trie, in particular, we try to find the longest one
    def contains(self, word, start):
        end_ix = -1
        node = self.root
        for i in range(start, len(word)):
            ch = word[i]
            ix = self.chartToIndex(ch)
            if not node.children[ix]:
                return end_ix

            # move to the next node because the character is found
            # and we have to look on it to see if it is the end of a word
            # or if we just ave to keep traversing the tree
            node = node.children[ix]

            # if the current substring matches a word in the trie,
            # we update the end_ix because we're looking for the longest word
            if node.is_end:
                end_ix = i

        return end_ix

class Solution:
    def minExtraChar(self, s, dictionary):
        # build the trie
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        count = 0
        i = 0
        # iterate over all characters of the string to see if we can find
        # a word in the trie that starts from the current character
        while i < len(s):
            ix = trie.contains(s, i)
            # if we don't find any word in the trie starting from the current character
            if ix == -1:
                # increment the counter of extra characters
                count += 1
                # and move to the next character
                i += 1
            else:
                # if we find a word, we skip all the characters of the word
                # and move to the first character after the word's end
                i = ix + 1

        return count

# solution two using a trie and dynamic programming
# Complexity:
# O(nm + s^2) time - where n is the number of words in the dictionary and m is the average length of the words in the dictionary
# and s is the length of the string s because we have to iterate over all the characters of the string in case it doesn't contain any word from the dictionary
# O(nm + d) space - to store the words in the trie and the DP array (d is the length of the string s)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minExtraChar(self, s, dictionary):
        # building the trie from the dictionary
        root = self.buildTrie(dictionary)
        n = len(s)
        # DP array to store minimum extra characters
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            # default case: considering current character as extra
            dp[start] = dp[start + 1] + 1

            node = root
            for end in range(start, n):
                # ensure the character is a lowercase letter
                if 'a' <= s[end] <= 'z':
                    if s[end] not in node.children:
                        # no further word can be formed
                        break
                    node = node.children[s[end]]
                    # if the current substring matches a word in the trie
                    if node.isEnd:
                        # this ensures that we remove the matched word from the count
                        # of extra characters and count the rest as extra characters
                        dp[start] = min(dp[start], dp[end + 1])
                else:
                    raise ValueError(f"Invalid character {s[end]} in string")

        # minimum extra characters for the entire string
        return dp[0]

    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                # ensure the character is a lowercase letter
                if 'a' <= char <= 'z':
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                else:
                    raise ValueError(f"Invalid character {char} in dictionary word {word}")
            node.is_end = True

        return root