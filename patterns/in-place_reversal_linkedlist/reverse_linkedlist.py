# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6394905626086d487e96e724

'''Problem:
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
'''

# solution one
# Complexity:
# 0(n) time - where n is the number of nodes in the linked list
# 0(1) space
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        # with 1 -> 2 -> 3 -> 4 -> 5 -> None,
        # at first iteration, head starts as 1
        # at second iteration, head becomes 2
        while head is not None:
            # at first iteration, next is 2
            # at second iteration, next is 3
            next = head.next
            # at first iteration, head is 1 and head.next becomes None instead of 2
            # at second iteration, head is 2 and head.next becomes 1 instead of 3
            head.next = prev
            # at first iteration, prev becomes 1
            # at second iteration, prev becomes 2
            prev = head
            # at first iteration, head becomes 2
            # at second iteration, head becomes 3
            head = next
        # after all iterations, prev becomes 5, which is the new head of the reversed linked list
        return prev
