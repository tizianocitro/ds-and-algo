# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64c2049b13a8a4eb9452a6d6

'''Problem:
Given the head node of a singly linked list, modify the list such that any node that has a node with a greater value to its right gets removed.
The function should return the head of the modified list.

Input: 5 -> 3 -> 7 -> 4 -> 2 -> 1
Output: 7 -> 4 -> 2 -> 1
Explanation: 5 and 3 are removed as they have nodes with larger values to their right.

Input: 7 -> 3 -> 5 -> 4 -> 2 -> 1
Output: 7 -> 5 -> 4 -> 2 -> 1
Explanation: 5 and 3 are removed as they have nodes with larger values to their right.
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the linked list
# O(n) space - because we are using a stack to store the nodes,
# and, in the worst case, when the list is sorted in ascending order,
# all the nodes will be pushed onto the stack, requiring n space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head):
        stack = []
        while head is not None:
            # remove nodes from the stack that are smaller than the current node
            while stack and stack[-1].val < head.val:
                stack.pop()
            # update the next pointer of the top node in the stack,
            # in case we have removed a middle node, so the prev node should now point at middle.next
            if stack:
                stack[-1].next = head
            stack.append(head)
            head = head.next
        
        while stack:
            head = stack.pop()

        return head
