# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1e63eb231098e09f3c6b1

'''Problem:
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
'''

# solution one
# Complexity:
# O(nlogn) - where n is the number of characters in the input string
# O(n) - to store the frequency of each character
from heapq import *

class Solution:
    def rearrangeString(self, str1):
        frequencies = {}
        for c in str1:
            frequencies[c] = frequencies.get(c, 0) + 1

        # add all characters to a max heap, so that we can add them to the result string
        # in a sorted order based on the frequency. In each step, we append one occurrence of the
        # highest frequency character to the results string. We will not put this character back in the heap
        # to ensure that no two same characters are adjacent to each other. In the next step, we process
        # the next most frequent character from the heap in the same way and then, at the end of this step,
        # insert the character from the previous step back to the heap after decrementing its frequency.
        max_heap = []
        for c, frequency in frequencies.items():
            heappush(max_heap, (-frequency, c))

        rearranged_str = []
        prev = None
        while max_heap:
            frequency, c = heappop(max_heap)

            # add the prev character back in the heap if its frequency
            # is greater than zero, meaning it can still be added again to the result string
            if prev and prev[0] > 0:
                heappush(max_heap, (-prev[0], prev[1]))

            # append the current character to the result string,
            # decrement its count and set it as the prev character
            rearranged_str.append(c)
            frequency = (-frequency) - 1
            prev = (frequency, c)

        # if we were successful in appending all the characters to the result string,
        # return it, otherwise return the empty string to indicate failure
        return ''.join(rearranged_str) if len(rearranged_str) == len(str1) else ''