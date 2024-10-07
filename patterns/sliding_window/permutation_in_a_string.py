# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6385d76c4a29c96532f7c16b

'''Problem:
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
1. "abc"
2. "acb"
3. "bac"
4. "bca"
5. "cab"
6. "cba"
If a string has n distinct characters, it will have n! permutations.

Input: string = "oidbcaf", pattern = "abc"   
Output: true   
Explanation: The string contains "bca" which is a permutation of the given pattern.

Input: string = "odicf", pattern = "dc"   
Output: false  
Explanation: No permutation of the pattern is present in the given string as a substring.
'''

# solution one
# Complexity:
# O(n + m) time - where n is the number of characters in the string and m is the number of characters in the pattern
# O(m) space - where m is the number of characters in the pattern
class Solution:
    def findPermutation(self, str1, pattern):
        k = len(pattern)
        chars_frequencies = {}
        start, matched = 0, 0

        for i in range(len(pattern)):
            char = pattern[i]
            chars_frequencies[char] = chars_frequencies.get(char, 0) + 1

        for end in range(len(str1)):
            char = str1[end]
            if char in chars_frequencies:
                chars_frequencies[char] -= 1
                # if the frequency of a character becomes 0, we have a complete match for that character
                if chars_frequencies[char] == 0:
                    matched += 1

            # matched is increased when the frequency of a char in the dict becomes 0,
            # meaning we have found a complete match for that char in the pattern.
            # If at any time, the number of characters matched is equal to the number of distinct characters in the pattern
            # (i.e., total characters in the HashMap), we have gotten our required permutation.
            if matched == len(chars_frequencies):
                return True

            # we are looking for a permutation of length k (pattern length),
            # so we shrink the window by one character from the beginning
            # at any iteration after the end pointer has processed k - 1 characters,
            # k -1 because the end pointer is 0-based indexed
            if end >= k - 1:
                char = str1[start]
                if char in chars_frequencies:
                    if chars_frequencies[char] == 0:
                        matched -= 1
                    chars_frequencies[char] += 1
                start += 1

        return False

# solution two
# Complexity:
# O(n + m) time - where n is the number of characters in the string and m is the number of characters in the pattern
# O(m + c) space - where m is the number of characters in the pattern and c is the number of unique characters in the pattern
class Solution:
    def findPermutation(self, str1, pattern):
        k = len(pattern)
        chars = set(pattern)
        chars_frequencies = {}
        start = 0
        
        for i in range(len(pattern)):
            char = pattern[i]
            chars_frequencies[char] = chars_frequencies.get(char, 0) + 1

        for end in range(len(str1)):
            char = str1[end]
            if char in chars:
                chars_frequencies[char] -= 1
                if chars_frequencies[char] <= 0:
                    del chars_frequencies[char]

            # it is possible to use a while loop as follow, it is the same
            # if end - start + 1 > k:
            while end - start + 1 > k:
                char = str1[start]
                if char in chars:
                    chars_frequencies[char] = chars_frequencies.get(char, 0) + 1
                    start += 1

            # this has to be here because if the elements in the range of the window
            # before shrinking it match the condition, it will return True, so we to shrink the window first
            if len(chars_frequencies) == 0:
                return True

        return False
