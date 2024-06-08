# !difficulty: medium

'''Problem:
Given the head of a LinkedList and a number k, reverse every alternating k sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than k elements, reverse it too.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> null, k = 2
Output: 2 -> 1 -> 3 -> 4 -> 6 -> 5 -> 7 -> 8 -> null
'''

# solution one using the reverseSubList method, which reverses a sub-list from p to q
# Complexity:
# 0(n) time - where n is the number of nodes in the linked list
# 0(1) space
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head, k):
        if k <= 1 or head is None:
            return head

        p, q, size = 1, k, self.getSize(head)
        current = head
        while p < size:
            current = self.reverseSubList(current, p, q)
            # During the first iteration, we're always changing the head, so we need to update it
            if p == 1:
                head = current
            p += (k * 2)
            q += (k * 2)
            # In case in the end we are left with a sub-list with less than k elements
            if q > size:
                q = size
        return head

    def reverseSubList(self, head, p, q):
        prev, current = None, head
        i = 1
        while current is not None and i < p:
            prev = current
            current = current.next
            i += 1

        last_node_first_part = prev
        last_node_sublist = current

        i = p
        while current is not None and i < q + 1:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1

        if last_node_first_part is None:
            head = prev
        else:
            last_node_first_part.next = prev
        
        last_node_sublist.next = current

        return head

    def getSize(self, head):
        size, current = 0, head
        while current is not None:
            size += 1
            current = current.next
        return size

# solution two reversing the sub-lists in a while loop
# Complexity:
# 0(n) time - where n is the number of nodes in the linked list
# 0(1) space
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head, k):
        if k <= 1 or head is None:
            return head

        current, prev = head, None
        while True:
            # the end of the previous part
            last_node_of_previous_part = prev
            
            # after reversing the LinkedList 'current' will become the last node of the sub-list
            last_node_of_sub_list = current

            i = 0
            # reverse k nodes in this iteration
            while current is not None and i < k:
                next = current.next
                current.next = prev
                prev = current
                current = next
                i += 1

            if last_node_of_previous_part is None:
                head = prev
            else:
                last_node_of_previous_part.next = prev

            # now the old current points to the new current
            # because the old current is now the last node of the sub-list
            # and the new current is the head of the next sub-list
            last_node_of_sub_list.next = current

            # if current is None, then we have reached the end of the LinkedList
            # this can be removed if the while condition at line 90 is changed to
            # while current is not None:
            if current is None:
                break

            # current is now the head of the next sub-list
            # so prev will be the last node of the previous sub-list
            prev = last_node_of_sub_list

            i = 0
            while current is not None and i < k:
                prev = current
                current = current.next
                i += 1

        return head
