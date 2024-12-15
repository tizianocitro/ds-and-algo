# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639cb0c8f9c10047d0529044

'''Problem:
Given a string, find all of its permutations preserving the character sequence but changing case.

The given string consists of lowercase English letters, uppercase English letters, and digits.

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
'''

# solution one
# the idea is that in each step, when we process the new character, we take all the permutations
# of the previous step and change the case of the letter in them in the same position to create the new permutations.
# Complexity:
# O(n * 2^n) time - where n is the number of elements in the input string
# This is because, for each character, two permutations are added to the deque.
# Therefore, the number of permutations grows exponentially with the length of s.
# E.g., after processing the first character, there are 2 permutations;
# after processing the second character, there are 4 permutations;
# after processing the third character, there are 8 permutations, and so on.
# O(n * 2^n) space - because we we will have 2^n permutations and each permutation has n elements
class Solution:
    def findLetterCaseStringPermutations(self, str):
        permutations = []
        permutations.append('')

        # process every character of the string one by one
        for i in range(len(str)):
            # only process characters, skip digits
            if str[i].isalpha():
                # we will take all existing permutations and change the letter case appropriately
                n = len(permutations)

                for j in range(n):
                    chs = list(permutations[j])
                    # if the current char is in upper case, change it to lower case or vice versa
                    chs[i] = chs[i].swapcase()
                    permutations.append(''.join(chs))

        return permutations

# solution two with queue and array
# Complexity:
# O(n * 2^n) time - where n is the number of elements in the input string
# This is because, for each character, two permutations are added to the deque.
# Therefore, the number of permutations grows exponentially with the length of s.
# E.g., after processing the first character, there are 2 permutations;
# after processing the second character, there are 4 permutations;
# after processing the third character, there are 8 permutations, and so on.
# O(n * 2^n) space - because we we will have 2^n permutations and each permutation has n elements
from collections import deque

class Solution:
    def findLetterCaseStringPermutations(self, s):
        result = []

        # it is a queue because at each iteration we want to start
        # with the permutations from the previous iteration
        permutations = deque()
        permutations.append([])

        for char in s:
            n_permutations = len(permutations)

            for _ in range(n_permutations):
                permutation = permutations.popleft()

                lower_permutation = list(permutation)
                lower_permutation.append(char.lower())

                # we do not want to add the number again because the case does not change
                if not char.isdigit():
                    upper_permutation = list(permutation)
                    upper_permutation.append(char.upper())

                if len(lower_permutation) == len(s):
                    result.append(''.join(lower_permutation))
                    if not char.isdigit():
                        result.append(''.join(upper_permutation))
                else:
                    permutations.append(lower_permutation)
                    if not char.isdigit():
                        permutations.append(upper_permutation)

        return result
