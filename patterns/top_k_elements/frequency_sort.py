# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1d17973a7d4466d460750

'''Problem:
Given a string, sort it based on the decreasing frequency of its characters.

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of unique characters in the input string
# in the worst case, when all characters are unique, we need to sort all of them which will take O(nlogn) time
# O(n) space - where n is the number of unique characters in the input string
# in the worst case, when all characters are unique, we need O(n) space for the map and the heap
from heapq import *

class Solution:
    def sortCharacterByFrequency(self, str):
        # find the frequency of each character
        frequencies = {}
        for char in str:
            frequencies[char] = frequencies.get(char, 0) + 1

        # add all characters to a max heap
        max_heap = []
        for k, v in frequencies.items():
            heappush(max_heap, (-v, k))

        # build a string, appending the most occurring characters first
        sorted_string = []
        while max_heap:
            frequency, char = heappop(max_heap)
            for _ in range(-frequency):
                sorted_string.append(char)
        
        return ''.join(sorted_string)

        # it could be done in this way as well but it is less efficient
        # sorted_string = ''
        # while max_heap:
        #    frequency, char = heappop(max_heap)
        #    sorted_string += char * -frequency
        # return sorted_string

