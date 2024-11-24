# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64902bd715f14528a3ef7363

'''Problem:
Given a stack, sort it using only stack operations (push and pop).
You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
The values in the stack are to be sorted in descending order, with the largest elements on top.

Input: [34, 3, 31, 98, 92, 23]
Output: [3, 23, 31, 34, 92, 98]

Input: [20, 10, -5, -1]
Output: [-5, -1, 10, 20]
'''

# solution one
# Complexity:
# O(n^2) time - because in the worst case, for every element that we pop from the input stack,
# we might have to pop all the elements in the temporary stack (and push them back to the original stack)
# to find the correct place to insert the element
# O(n) space - because of the temporary stack to store the sorted elements
class Solution:
    def sortStack(self, stack):
        if len(stack) < 2:
            return stack

        # a stack to store the sorted elements
        sortedStack = []

        # continue sorting until the original stack is empty
        while stack:
            top = stack.pop()

            # move elements from the temporary stack back to the original stack
            # until we find the correct position for the current element
            while sortedStack and sortedStack[-1] > top:
                stack.append(sortedStack.pop())

            # place the current element in its correct sorted position in the temporary stack
            sortedStack.append(top)

        return sortedStack