# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f23b94e4f288d4a83ae0d

'''Problem:
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given key.

Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter.
This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given key.

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
'''

# solution one using a next_letter variable
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def searchNextLetter(self, letters, key):
        # in case we don't find the next letter in the array,
        # the next letter will be the first letter of the array
        next_letter = letters[0]

        left, right = 0, len(letters) - 1
        while left <= right:
            middle = (left + right) // 2
            current = letters[middle]

            # ord could be removed and just compare the letters (e.g., solution three)
            if ord(current) > ord(key):
                next_letter = current
                right = middle - 1
            else: # if it's equal or smaller, we move ahead
                left = middle + 1

        return next_letter

# solution two using left pointer position
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def searchNextLetter(self, letters, key):
        left, right = 0, len(letters) - 1
        while left <= right:
            middle = (left + right) // 2
            current = letters[middle]

            # ord could be removed and just compare the letters (e.g., solution three)
            if ord(current) > ord(key):
                right = middle - 1
            else:
                left = middle + 1

        return letters[left % len(letters)]

# solution three using left pointer position, same as solution two but without ord()
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def searchNextLetter(self, letters, key):
        left, right = 0, len(letters) - 1
        while left <= right:
            middle = (left + right) // 2
            current = letters[middle]

            if current > key:
                right = middle - 1
            else:
                left = middle + 1

        return letters[left % len(letters)]
