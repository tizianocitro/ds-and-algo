# !code: 139, !difficulty: medium, !from: https://leetcode.com/problems/word-break/

'''Problem:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
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
    def wordBreak(self, s: str, word_dict) -> bool:
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