# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/split-a-string-into-the-max-number-of-unique-substrings-medium

'''Problem:
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string.
However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.
s contains only lower case English letters.

Input: s = "aab"  
Output: 2  
Explanation: Two possible ways to split the given string into maximum unique substrings are: ['a', 'ab'] & ['aa', 'b'], both have 2 substrings; hence the maximum number of unique substrings in which the given string can be split is 2.

Input: s = "abcabc"  
Output: 4  
Explanation: Four possible ways to split into maximum unique substrings are: ['a', 'b', 'c', 'abc'] & ['a', 'b', 'cab', 'c'] &  ['a', 'bca', 'b', 'c'] & ['abc', 'a', 'b', 'c'], all have 4 substrings.
'''

# solution one
# Complexity:
# O(2^n) time - where n is the length of the input string s
# because there is only 2^n possible ways to split any given string of length n
# O(n) space - where n is the length of the input string s
# as we need to save only one way of splitting the given string while in the recursion, 
# and so, the recursion tree won't get bigger than O(n) steps too
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.splitAndCount(s, 0, set())

    def splitAndCount(self, s, start, unique_subs):
        n = len(s)
        # base case, if we have reached the end of the input string, return the size of the set
        if start == n:
            return len(unique_subs)

        count = 0
        # loop through all substrings starting from the current start position
        for i in range(start + 1, n + 1):
            sub = s[start:i]
            # if the substring is not in the set, add it and recursively
            # call the function with the new start position to check all
            # possible substrings starting with the start position
            if sub not in unique_subs:
                unique_subs.add(sub)
                count = max(count, self.splitAndCount(s, i, unique_subs))
                # remove the substring from the set and backtrack
                unique_subs.remove(sub)

        # return the maximum count of unique substrings found
        return count
