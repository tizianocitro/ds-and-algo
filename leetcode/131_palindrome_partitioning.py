# !code: 131, !difficulty: medium, !from: https://leetcode.com/problems/palindrome-partitioning, https://neetcode.io/problems/palindrome-partitioning

'''Problem:
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]
'''

# solution one using backtracking
# Complexity:
# O(n * 2^n) time - where n is the length of the string, because in the worst case we explore all possible ways
# to partition the string (2^n partitions), and for each partition we check if substrings are palindromes (O(n))
# O(n * 2^n) space - where n is the length of the string, due to storing all partitions in the result (2^n partitions
# with average length n), and O(n) for recursion call stack depth (because we explore partitions character by character, so each index) and the part list
class Solution:
    def partition(self, s: str):
        result = []
        # start from the first character as it forms a palindrome or the start of a palindrome substring
        self.backtract_partition(0, 0, s, [], result)
        return result

    # goes through the string in a dfs-like manner
    def backtract_partition(self, i, j, s, part, result):
        # base case: j has reached the end of the string
        # it works the same as:
        # if i == len(s):
        if j >= len(s):
            # if i also reached the end, it means the entire string was partitioned
            # (no leftover characters between i and j)
            if i == j:
                # valid partition found, so we add a copy to results
                result.append(part.copy())
            # backtrack regardless (either valid partition saved or invalid path terminated)
            return

        # if the substring between i and j is a palindrome, we can include it in the current partition
        # and explore the next string starting from j + 1 to be part of the same partition
        if self.is_palindrome(i, j, s):
            part.append(s[i:j + 1])
            self.backtract_partition(j + 1, j + 1, s, part, result)

            # remove the last added substring to backtrack and explore partitions without it
            part.pop()

        # explore the next character to see if the substring from i to j + 1 can form a palindrome
        self.backtract_partition(i, j + 1, s, part, result)    

    def is_palindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
