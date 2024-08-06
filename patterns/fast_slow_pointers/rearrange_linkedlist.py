# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63923313ae2ec690ac22b61d

''' Problem:
Given the head of a Singly LinkedList, write a method to modify the LinkedList
such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.
So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should use only constant space the input LinkedList should be modified in-place.

Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the linked list
# O(1) space
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reorder(self, head):
        if head is None or head.next is None:
            return head

        headSecondHalf = self.getHeadSecondHalf(head)
        headSecondHalf = self.reverse(headSecondHalf)

        self.reorderList(head, headSecondHalf)

        return head

    def getHeadSecondHalf(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        # starts as None because the last node has to point to None
        prev = None

        # while we don't reach the next of the original last node
        while head is not None:
            # save next node before overriding
            next = head.next

            # change the next of the node to the previous node processed,
            # which originally was its precedessor
            head.next = prev

            # store the current node as the new precedessor for the next node
            prev = head

            # update the node to process the next node in the origina list
            head = next

        return prev

    def reorderList(self, headFirstHalf, headSecondHalf):
        while headFirstHalf is not None and headSecondHalf is not None:
            headFirstHalfNext = headFirstHalf.next
            headSecondHalfNext = headSecondHalf.next

            headFirstHalf.next = headSecondHalf
            headSecondHalf.next = headFirstHalfNext

            headFirstHalf = headFirstHalfNext
            headSecondHalf = headSecondHalfNext

        if headFirstHalf is not None:
            headFirstHalf.next = None

