# !difficulty: hard

'''Problem:
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Input: string = "aabdec", pattern = "abc"  
Output: "abdec"  
Explanation: The smallest substring having all characters of the pattern is "abdec".

Input: string = "adcad", pattern = "abc"
Output: ""  
Explanation: No substring in the given string has all characters of the pattern.
'''

# solution one
# Complexity:
# O(n + m) time - where n is the number of characters in the string and m is the number of characters in the pattern
# O(m) space - where m is the number of characters in the pattern
# In the worst case, we also need O(n) space for the resulting substring, which will happen when the input string is a permutation of the pattern.
class Solution:
    def findSubstring(self, str1, pattern):
        min_length, start_index = float("inf"), 0
        start, matched = 0, 0
        char_frequencies = {}

        for char in pattern:
            char_frequencies[char] = char_frequencies.get(char, 0) + 1

        for end in range(len(str1)):
            char = str1[end]
            if char in char_frequencies:
                char_frequencies[char] -= 1
                if char_frequencies[char] == 0:
                    matched += 1
        
            # iterate until the match is present because
            # we want to shrink the window to reduce the length of the substring
            while matched == len(char_frequencies):
                current_length = end - start + 1
                if min_length > current_length:
                    min_length = current_length
                    start_index = start

                char = str1[start]
                if char in char_frequencies:
                    if char_frequencies[char] == 0:
                        matched -= 1
                    char_frequencies[char] += 1
                start += 1

        # if the substring is not present
        if min_length > len(str1):
            return ""

        # when you slice a string using string[start:end], the character at the end index is not included in the slice.
        # It means that the slice will include characters from the start index up to, but not including, the character at the end index.
        return str1[start_index:start_index + min_length]; 

# solution two
# Complexity:
# O(n + m) time - where n is the number of characters in the string and m is the number of characters in the pattern
# O(m) space - where m is the number of characters in the pattern
# In the worst case, we also need O(n) space for the resulting substring, which will happen when the input string is a permutation of the pattern.
class Solution:
    def findSubstring(self, str1, pattern):
        window_start, matched, substr_start = 0, 0, 0
        min_length = len(str1) + 1
        char_frequency = {}

        for chr in pattern:
            if chr not in char_frequency:
                char_frequency[chr] = 0
            char_frequency[chr] += 1

        # try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                # Count every matching of a character
                if char_frequency[right_char] >= 0:
                    matched += 1

            # Shrink the window if we can, finish as soon as we remove a matched character
            while matched == len(pattern):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start

                left_char = str1[window_start]
                window_start += 1
                if left_char in char_frequency:
                    # We could have redundant matching characters, therefore we'll
                    # decrement the matched count only when a useful occurrence of a matched
                    # character is going out of the window
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        if min_length > len(str1):
            return ""
        return str1[substr_start:substr_start + min_length]