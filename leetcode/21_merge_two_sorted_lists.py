# !code: 21, !difficulty: easy, !from: https://leetcode.com/problems/merge-two-sorted-lists/

'''Problem:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Constraints:
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
'''

# solution one using two pointers
# Complexity:
# O(n + m) time - where n is the length of list1 and m is the length of list2
# O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()

        curr = dummy

        # until we reach the end of both lists and we manage
        # edge cases by considering float('inf') as the value of the node
        # when one of the two lists is empty or we have reached its end
        while list1 or list2:
            l1_val = list1.val if list1 else float('inf')
            l2_val = list2.val if list2 else float('inf')

            # always insert the node with the smaller value first
            # and then move the pointer to the next node
            if l1_val < l2_val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        return dummy.next

# solution two less clean
# Complexity:
# O(n + m) time - where n is the length of list1 and m is the length of list2
# O(1) space
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)

        head = dummy
        while list1 or list2:
            # only list2 has nodes left
            if not list1 and list2:
                head.next = list2
                list2 = list2.next
            # only list1 has nodes left
            elif list1 and not list2:
                head.next = list1
                list1 = list1.next
            # both lists have nodes left, insert the smaller one
            else:
                if list1.val <= list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next

            head = head.next

        return dummy.next