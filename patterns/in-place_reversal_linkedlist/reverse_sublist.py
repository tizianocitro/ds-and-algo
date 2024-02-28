# !difficulty: medium

'''Problem:
Given the head of a LinkedList and two positions p and q, reverse the LinkedList from position p to q.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> None, p = 2, q = 4
Output: 1 -> 4 -> 3 -> 2 -> 5 -> None
'''

'''Similar problems:
Problem 1: Reverse the first k elements of a given LinkedList.
Solution: This problem can be easily converted to the parent problem; to reverse the first k nodes of the list, we need to pass p=1 and q=k.

Problem 2: Given a LinkedList with n nodes, reverse it based on its size in the following way:
- If n is even, reverse the list in a group of n/2 nodes.
- If n is odd, keep the middle node as it is, reverse the first n/2 nodes and reverse the last n/2 nodes.
Solution:
When n is even we can perform the following steps:
1. Reverse first n/2 nodes: head = reverse(head, 1, n/2)
2. Reverse last n/2 nodes: head = reverse(head, n/2 + 1, n)
When n is odd, our algorithm will look like:
1. head = reverse(head, 1, n/2)
2. head = reverse(head, n/2 + 2, n)
In the second step, we’re skipping two elements as we will be skipping the middle element if n is odd.
'''

# solution one with for loops
# Complexity:
# 0(n) time - where n is the number of nodes in the linked list
# 0(1) space
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head, p, q):
        if p == q:
            return head

        prev, succ, current = None, head, head
        # find the successor of the node at q to become the successor of the node at p
        for _ in range(1, q + 1):
            succ = succ.next
        # find the node at p and its predecessor, which is the node at p - 1
        # the node at p - 1 will become the predecessor of the node currently at q
        for _ in range(1, p):
            prev = current
            current = current.next

        for _ in range(p, q + 1):
            next = current.next
            current.next = succ
            succ = current
            current = next

        # if prev is None it means p = 1, so we're switching the head
        if prev is None:
            return succ
        prev.next = succ

        return head

# solution two with while loops
# Complexity:
# 0(n) time - where n is the number of nodes in the linked list
# 0(1) space
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head, p, q):
        if p == q:
            return head

        # after skipping 'p-1' nodes, current will point to 'p'th node
        current, previous = head, None
        i = 0
        while current is not None and i < p - 1:
            previous = current
            current = current.next
            i += 1

        # we are interested in three parts of the LinkedList, the part before index 'p',
        # the part between 'p' and 'q', and the part after index 'q'
        last_node_of_first_part = previous

        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current

        # will be used to temporarily store the next node
        next = None

        i = 0
        # reverse nodes between 'p' and 'q'
        while current is not None and i < q - p + 1:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the first part
        if last_node_of_first_part is not None:
            # 'previous' is now the first node of the sub-list
            last_node_of_first_part.next = previous
        else: # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
            head = previous

        # connect with the last part
        last_node_of_sub_list.next = current

        return head

# solution three with while loops but easier to understand
# it uses the same approach as solution one for the indexes
# Complexity:
# 0(n) time - where n is the number of nodes in the linked list
# 0(1) space
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head, p, q):
        if p == q:
            return head

        # after skipping 'p-1' nodes, current will point to 'p'th node
        current, prev = head, None
        i = 1
        while current is not None and i < p:
            prev = current
            current = current.next
            i += 1

        # we are interested in three parts of the LinkedList, the part before index 'p',
        # the part between 'p' and 'q', and the part after index 'q'
        last_node_of_first_part = prev

        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current

        i = p
        # reverse nodes between 'p' and 'q'
        while current is not None and i < q + 1:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1

        # connect with the first part
        if last_node_of_first_part is None:
            # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
            head = prev
        else:
            # 'previous' is now the first node of the sub-list
            last_node_of_first_part.next = prev

        # connect with the last part
        # this is the node at position p before the swap,
        # it will point to its precedessor before, so we need to point it to the current node,
        # which will be node at position q + 1, so the successor of the node that was at position q
        last_node_of_sub_list.next = current

        return head
