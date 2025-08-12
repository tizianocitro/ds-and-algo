# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/word-break-medium

'''Problem:
Given a non-empty string and a dictionary containing a list of non-empty words,
determine if the string can be segmented into a space-separated sequence of one or more dictionary words.
Each word in the dictionary can be reused multiple times.

Input:
    String: "ilovecoding"
    Dictionary: ["i", "love", "coding"]
Output: True
Explanation: The string can be segmented as "i love coding".

Input:
    String: "helloworld"
    Dictionary: ["hello", "world", "hell", "low"]
Output: True
Explanation: The string can be segmented as "hello world".

Input:
    String: "enjoylife"
    Dictionary: ["enj", "life", "joy"]
Output: False
Explanation: Despite having the words "enj" and "life" in the dictionary, we can't segment the string into the space-separated dictionary words.
'''

'''Note:
At https://leetcode.com/problems/word-break/ you can find a solution that uses a Trie data structure or a Depth First Search (DFS) algorithm.
There are also other two approaches that use dynamic programming and have a different time complexity (maybe better).
'''

# solution one using dynamic programming
# Complexity:
# O(n^3 + m) time - where n is the length of the string and m is the number of words in the dictionary
# due to the two nested loops where we check all possible substrings
# and the slicing operation s[j:i] which takes O(n) time
# m is for converting the list of words to a set
# O(n + m) space - where n is the length of the string (for the queue and the seen set)
# and m is the number of words in the dictionary (for the dictionary set)
class Solution:
    def wordBreak(self, s, word_dict):
        # convert the list of words to a set for faster lookup
        # this takes O(m) time where m is the number of words in the dictionary
        dictionary = set(word_dict)

        n = len(s)

        # dp[i] is True if the substring s[:i] can be segmented into words in the dictionary
        # we need n + 1 because we need to consider the empty string,
        # so the string s starts from index 1 of this array
        dp = [False for _ in range(n + 1)]

        # an empty string can always be segmented
        dp[0] = True

        # iterate over the string
        for i in range(1, n + 1):
            # iterate over the string from the beginning to the current index
            # so consider all the substrings from the beginning to the current index
            for j in range(i):
                # get the substring from j to i
                # this takes O(n) time where n is the length of the string
                word = s[j:i]
                # if the substring up to j can be segmented and
                # the substring from j to i is in the dictionary
                if dp[j] and word in dictionary:
                    # then the substring up to i can be segmented
                    dp[i] = True
                    # the break is to avoid unnecessary iterations
                    # but it doesn't affect the correctness of the solution
                    # so it can be removed
                    break

        # at the end, the result will be in the last index
        # because it will contain True if the whole string can be segmented
        return dp[n]

# solution two using bottom-up dynamic programming
# Complexity:
# O(n^2 * m) time - where n is the length of the string and m is the number of words in the dictionary
# because for each index of the string (length of n), we check all the m words in the dictionary and
# the slicing operation s[i - len(word):i] takes O(n) time
# O(n) space - to store the results of the subproblems
class Solution:
    def wordBreak(self, s: str, word_dict) -> bool:
        # dp[i] is True if the substring s[:i] can be
        # segmented into words in the dictionary
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in word_dict:
                # handle out of bounds case for when
                # the word is longer than the current substring
                if i < len(word) - 1:
                    continue

                # if the current substring is equal to the word
                # or the previous substring is a valid word
                if i == len(word) - 1 or dp[i - len(word)]:
                    # this takes O(n) time where n is the length of the string
                    word_to_check = s[i - len(word) + 1 : i + 1]
                    if word_to_check == word:
                        dp[i] = True
                        break

        # the result will be in the last index
        return dp[-1]

# solution three using bfs
# Complexity:
# O(n^3 + m) time - where n is the length of the string and m is the number of words in the dictionary
# due to the two nested loops where we check all possible substrings
# and the slicing operation s[start:end] which takes O(n) time
# m is for converting the list of words to a set
# O(n + m) space - where n is the length of the string (for the queue and the seen set)
# and m is the number of words in the dictionary (for the dictionary set)
from collections import deque

class Solution:
    def wordBreak(self, s: str, word_dict) -> bool:
        # convert the list of words to a set for faster lookup
        dictionary = set(word_dict)

        # use the queue to perform a breadth-first search
        # starting from the first character of the string
        queue = deque([0])

        # keep track of the indices that have been visited
        seen = set()

        while queue:
            start = queue.popleft()

            # if we reach the end of the string
            # it means we can segment the string
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                # if the end index has been visited
                # we don't need to check it again
                if end in seen:
                    continue

                # if the substring from start to end is in the dictionary
                if s[start:end] in dictionary:
                    queue.append(end)
                    seen.add(end)

        return False