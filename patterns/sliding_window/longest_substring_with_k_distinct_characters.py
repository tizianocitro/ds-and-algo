# !difficulty: medium

'''Problem:
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Input: string = "araaci", k = 2
Output: 4  
Explanation: The longest substring with no more than 2 distinct characters is "araa".
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input string
# O(k) space - where k is the number of distinct characters in input,
# as we will be storing a maximum of k + 1 characters in the dictionary
class Solution:
    def findLength(self, str1, k):
        max_length = 0
        start = 0
        char_frequencies = {}

        for end in range(len(str1)):
            # instead of end - start we can also create a length var to increase by 1 in the for loop
            # and decrease by 1 in the while len(char_frequencies) > k loop
            # this can also be done at the end of the for loop but it then should be:
            # max_length = max(max_length, end - start + 1)
            max_length = max(max_length, end - start)
            char = str1[end]
            char_frequencies[char] = char_frequencies.get(char, 0) + 1

            # shrink the sliding window until we are left with k distinct chars in the char_frequencies
            while len(char_frequencies) > k:
                char = str1[start]
                char_frequencies[char] -= 1
                if char_frequencies[char] <= 0:
                    del char_frequencies[char]

                # shrink the window
                start += 1

        return max_length

# solution two with lenght update at the end of the loop
# Complexity:
# O(n) time - where n is the length of the input string
# O(k) space - where k is the number of distinct characters in input,
# as we will be storing a maximum of k + 1 characters in the dictionary
class Solution:
    def findLength(self, str1, k):
        max_length = 0
        start = 0
        char_frequencies = {}

        for end in range(len(str1)):
            char = str1[end]
            char_frequencies[char] = char_frequencies.get(char, 0) + 1

            # shrink the sliding window until we are left with k distinct chars in the char_frequencies
            while len(char_frequencies) > k:
                char = str1[start]
                char_frequencies[char] -= 1
                if char_frequencies[char] <= 0:
                    del char_frequencies[char]

                # shrink the window
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length