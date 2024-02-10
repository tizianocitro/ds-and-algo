# !difficulty: hard

'''Problem:
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string,
we get n! permutations (or anagrams) of a string having nn characters.
For example, here are the six anagrams of the string “abc”:
1. "abc"
2. "acb"
3. "bac"
4. "bca"
5. "cab"
6. "cba"
If a string has n distinct characters, it will have n! permutations.

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Input: string = "ppqp", pattern = "pq"  
Output: [1, 2]  
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Input: string = "abbcabc", pattern = "abc"  
Output: [2, 3, 4]  
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''

# solution one
# Complexity:
# O(n + m) time - where n is the number of characters in the string and m is the number of characters in the pattern
# O(m) space - where m is the number of characters in the pattern
class Solution:
    def findStringAnagrams(self, str1, pattern):
        result_indices = []
        char_frequiences = {}
        start, matched = 0, 0
        k = len(pattern)

        for char in pattern:
            char_frequiences[char] = char_frequiences.get(char, 0) + 1

        for end in range(len(str1)):
            char = str1[end]
            if char in char_frequiences:
                char_frequiences[char] -= 1
                if char_frequiences[char] == 0:
                    matched += 1
        
            # Have we found an anagram?
            # should be equivalent to len(char_frequiences) because we are checking if the entry for a character in the dictionary is 0
            # and it is 0 when the string has the same number of instances of that characters as the pattern
            if matched == len(char_frequiences):
                result_indices.append(start)
            
            if end >= k - 1:
                char = str1[start]
                if char in char_frequiences:
                    if char_frequiences[char] == 0:
                        # Before putting the character back, decrement the matched count if char_frequency is 0
                        matched -= 1
                    # Put the character back
                    char_frequiences[char] += 1
                start += 1

        return result_indices