# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6394ef9cc6ebad0cc48b8076

'''Problem:
Given the head of a Singly LinkedList and a number k, rotate the LinkedList to the right by k nodes.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, k = 3
Output: 4 -> 5 -> 6 -> 1 -> 2 -> 3 -> null
'''

'''Solution:
Another way of defining the rotation is to take the sub-list of k ending nodes of the LinkedList and connect them to the beginning.
Other than that we have to do three more things:
1. Connect the last node of the LinkedList to the head, because the list will have a different tail after the rotation.
2. The new head of the LinkedList will be the node at the beginning of the sublist.
3. The node right before the start of sub-list will be the new tail of the rotated LinkedList.
'''

# solution one
# Complexity:
# 0(n) time - where n is the number of nodes in the list
# 0(1) space - because we only used a few extra variables
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def rotate(self, head, rotations):
        # find the last node and calculate the size of the list
        # size starts at 1 because we don't want to process the last node and skip it,
        # we need the last node later on to point it to the head
        size, last = 1, head
        while last.next is not None:
            last = last.next
            size +=1

        # last node points to the head, in this way we
        # connect the last node with the head to make it a circular list
        last.next = head

        # normalize rotations on list's size,
        # because no need to do rotations more than the length of the list
        rotations = rotations % size

        # how many steps are needed to reach the node preceeding the one that should become the new head
        skips = size - rotations

        # iterate untile the node preceeding the one that should become the new head
        # at the end of the loop, current is pointing to the sub-list of k ending nodes
        current = head
        for _ in range(1, skips):
            current = current.next

        # the next of current node will be the new head
        head = current.next

        # the current node will be the new last of the list
        current.next = None

        return head

