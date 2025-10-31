# !code: 2, !difficulty: medium, !from: https://leetcode.com/problems/add-two-numbers/

'''Problem:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
So, it is guaranteed that the list represents a number that does not have leading zeros.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# solution one
# Complexity:
# O(n) time - where n is the size of the longest linked list
# O(n) space - where n is the size of the longest linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # dummy node for the managing the edge cases
        dummy = ListNode()

        # current node for the creation on the linked list for the result
        current = dummy

        # carry for sums greater than 10
        carry = 0
        # while we have nodes in any of the linked lists or carry is not 0
        while l1 or l2 or carry:
            # if a linked list has no more nodes, we set the value to 0
            # because we just take the value of the node that still exists
            # since node.val + 0 = node.val
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # sum the values of the nodes and the carry if present
            val = val1 + val2 + carry
            # the carry will be the first digit of the sum if greater than 10
            # otherwise it will be 0, because 9 + 9 = 18, so 18 // 10 = 1
            # but if 8 + 1 = 9, so 9 // 10 = 0 
            carry = val // 10
            # we want only the second digit of the sum, so we mod the sum by 10
            # 18 % 10 = 8, 9 % 10 = 9
            val %= 10

            # update the pointers in the linked lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # insert the new node in the result linked list
            # and move to the next node to insert
            current.next = ListNode(val)
            current = current.next

        # the head of the result linked list is the next node of the dummy node
        return dummy.next 

# solution two convert linked lists to numbers, sum the numbers and convert the result to a linked list
# Complexity:
# O(n) time - where n is the size of the longest linked list
# O(n) space - where n is the size of the longest linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # convert l1 to number
        l1_size = self.size(l1)
        l1_num = self.convert2Num(l1, l1_size)

        # convert l2 to number
        l2_size = self.size(l2)
        l2_num = self.convert2Num(l2, l2_size)

        # sum l1 and l2 to get the result
        num = l1_num + l2_num

        # build the linked list from the result
        head = ListNode()
        node = head
        i, size = 0, len(str(num))
        for c in reversed(str(num)):
            node.val = c
            if i < size - 1:
                node.next = ListNode()
                node = node.next
            i += 1
        return head

    def size(self, head):
        size = 0
        node = head
        while node is not None:
            size += 1
            node = node.next
        return size

    def convert2Num(self, head, size):
        num = 0
        node = head
        for i in range(size):
            # the first node has to be multiplied by 10^0 = 1
            # the second node has to be multiplied by 10^1 = 10
            # the third node has to be multiplied by 10^2 = 100 and so on
            # so if we have 2 -> 4 -> 3, we have to do 2*1 + 4*10 + 3*100 = 342
            num += int(node.val) * (10**i)
            node = node.next
        return num
