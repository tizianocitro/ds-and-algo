# !code: 206, !difficulty: easy, !from: https://leetcode.com/problems/reverse-linked-list/

'''Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000

Follow-Up Question:
A linked list can be reversed either iteratively or recursively. Could you implement both?

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
'''

# solution one iterative
# Complexity:
# O(n) time - where n is the number of nodes in the linked list
# O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        # we return prev because during the last iteration, head becomes None
        # and prev becomes the last node in the original linked list,
        # which is the new head of the reversed linked list
        # e.g., if the original linked list is 1 -> 2 -> 3 -> 4 -> 5 -> None,
        # after the last iteration, prev becomes 5, which is the new head of the reversed linked list
        # this is because we traverse the list until head becomes None (which happens after the last node 5)
        return prev

# solution two recursive
# Complexity:
# O(n) time - where n is the number of nodes in the linked list
# O(n) space - because of the recursive calls
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)

    def reverse(self, current, prev):
        # given the linked list 1 -> 2 -> 3 -> 4 -> 5 -> None
        # this happen when the last node is reached and calls self.reverse(None, 5)
        if not current:
            # prev here will be the new head of the reversed linked list
            return prev

        # reverse the list and keep track of the new head to propagate it back
        # to the first call of self.reverse(head, None) in self.reverseList()
        new_head = self.reverse(current.next, current)
        current.next = prev
        return new_head

'''Solution:
More details on this recursive solution: https://leetcode.com/problems/reverse-linked-list/editorial#approach-2-recursive
'''

# solution three recursive using another approach
# Complexity:
# O(n) time - where n is the number of nodes in the linked list
# O(n) space - because of the recursive calls
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
