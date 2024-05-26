# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1eb62b231098e09f3cc06

'''Problem:
Design a class that simulates a Stack data structure, implementing the following two operations:
1. push(int num): Pushes the number num on the stack.
2. pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

It is guaranteed that there will be at least one element in the stack before calling pop.

Explaination:
After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)

1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2
'''

# solution one, simpler but worse than solution two
# Complexity:
# O(nlogk) time - where n is the number of numbers in input and k is the number of numbers with the maximum frequency
# O(n) space -  where n is the number of numbers in input
# Complexity of the push and pop operations:
# push(): O(1) time
# pop(): O(nlogk) time - where n is the number of numbers in input and 
# k is the number of numbers with the maximum frequency that we will add into the heap
# push(): O(1) space
# pop(): O(n) space - for the frequencies map
from heapq import *

class Solution:

    # the stack needs O(n) space because it will store all
    # the numbers pushed into it and placeholders for popped numbers
    def __init__(self):
        self.stack = []

    # O(1) time | O(1) space
    def push(self, num):
        self.stack.append(num)

    # O(nlogk) time | O(n) space for the frequencies and O(k) space for the heap
    # because we only store the numbers with the maximum frequency in the heap
    def pop(self):
        max_freq = 0
        frequencies = {}
        for i, num in enumerate(self.stack):
            # skips inf because it is a placeholder for popped numbers
            if num == float('inf'):
                continue

            freq, _ = frequencies.get(num, (0, 0))
            freq += 1
            # always update the frequency of the number and
            # store the index of the last time we encountered it
            frequencies[num] = (freq, i)
            # keep track of the maximum frequency for a number
            max_freq = max(max_freq, freq)

        # insert in a max heap the numbers with the maximum frequency,
        # the index will be the key used for the heap because we want to
        # return the number that was pushed last in case of a tie, and in
        # case of no tie, there will be only one number in the heap, so we
        # can return it the same way because we are always interested in the top
        max_heap = []
        for num, frequency in frequencies.items():
            freq, ix = frequency
            if freq == max_freq:
                heappush(max_heap, (-ix, num))

        # pop the number with the highest index, which is also
        # the one with the highest frequency, and then update the stack
        # by adding inf as placeholder to indicate the number was popped
        most_repeating_ix, most_repeating_num = heappop(max_heap)
        self.stack[-most_repeating_ix] = float('inf')

        return most_repeating_num

# solution two, more complex but better than solution one
# Complexity:
# O(logn) time - where n is the number of numbers in input
# O(n) space -  where n is the number of numbers in input for the max heap and frequencies map
# Complexity of the push and pop operations:
# push(): O(logn) time - where n is the number of numbers in input because we are pushing to a heap
# pop(): O(logk) time - where n is the number of numbers in input because we are popping from a heap
# push(): O(1) space
# pop(): O(1) space
from heapq import *

class Element:

    def __init__(self, number, frequency, sequence_number):
        # number is the value of the number
        self.number = number
        # frequency is frequency of the number when it was pushed to the heap
        self.frequency = frequency
        # sequence_number is a used to keep track of order of numbers pushed to the heap,
        # to know what number was pushed first in case of a tie
        self.sequence_number = sequence_number

    # we need to use the __lt__ method to make the heap a max heap
    # in any case, the heap will always use the __lt__ method to compare
    # elements, so it is the method to customize when needed for custom classes
    def __lt__(self, other):
        # higher frequency wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency

        # if both elements have same frequency, return the element that was pushed later
        return self.sequence_number > other.sequence_number

class Solution:

    def __init__(self):
        self.sequence_number = 0
        self.max_heap = []
        self.frequencies = {}

    # O(logn) time | O(1) space
    def push(self, num):
        self.frequencies[num] = self.frequencies.get(num, 0) + 1
        # push the element each time we encounter it, with its frequency
        # at the time, as well as the sequence number to keep track of the order
        heappush(self.max_heap,
                Element(num, self.frequencies[num], self.sequence_number))
        # increment the sequence number for next push
        self.sequence_number += 1

    # O(logn) time | O(1) space
    def pop(self):
        # get the number with the maximum frequency
        num = heappop(self.max_heap).number

        # decrement the frequency or remove if this is the last number
        if self.frequencies[num] > 1:
            self.frequencies[num] -= 1
        else:
            # delete because the frequency is 1, so just reducing would set it to 0
            del self.frequencies[num]

        return num
