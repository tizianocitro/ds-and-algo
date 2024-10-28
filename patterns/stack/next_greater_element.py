# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/652377d9b28abf3c6db3b596

'''Problem:
Given an array, print the Next Greater Element (NGE) for every element.
The Next Greater Element for an element x is the first greater element on the right side of x in the array.
Elements for which no greater element exist, consider the next greater element as -1.

Input: [4, 5, 2, 25]
Output: [5, 25, 25, -1]
'''

'''Solution:
The algorithm leverages the nature of the stack data structure, where the most recently added (pushed) elements are the first ones to be removed (popped).
Starting from the end of the array, the algorithm always maintains elements in the stack that are larger than the current element.
This way, it ensures that it has a candidate for the "next larger element".
If there is no larger element, it assigns -1 to that position.
It handles each element of the array only once, making it an efficient solution.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - where n is the length of the input array
class Solution:
    def nextLargerElement(self, arr):
        # equivalent to res = [-1 for _ in range(len(arr))]
        res = [-1] * len(arr)

        stack = []

        # start from the end so that we can levarge stack property of having
        # the last processed element on top
        for i in reversed(range(len(arr))):
            el = arr[i]

            # remove all elements in the stack that are lower than the current number,
            # the element at the top of the stack (stack[-1]) will always be the element
            # right next to the current, so in [2, 1, 3], when processing 2,
            # the top will first be 1, than 3. This is also why we first remove lower numbers
            while stack and stack[-1] <= el:
                stack.pop()
            
            # elements are -1 by default so no need to worry about
            # the case the stack is empty, so the element has no higher number on the right
            if stack:
                res[i] = stack[-1]
            stack.append(el)

        return res
