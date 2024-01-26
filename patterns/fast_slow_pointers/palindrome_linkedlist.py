# !difficulty: medium

'''
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished.
The algorithm should have O(N) time complexity where N is the number of nodes in the LinkedList.

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the LinkedList
# O(q) space
# 1. We use the Fast & Slow pointers method to get the middle of the LinkedList;
# 2. Once we have the middle, we reverse the second half;
# 3. Then, we compare the first half with the reversed second half to see if the LinkedList represents a palindrome;
# 4. Finally, we reverse the second half of the LinkedList again to revert and bring the LinkedList back to its original form.
class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # find middle of the LinkedList
        slow, fast = head, head
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        head_second_half = self.reverse(slow)

        # store the head of reversed part to revert back later
        copy_head_second_half = head_second_half

        # compare the first and the second half
        while head is not None and head_second_half is not None:
            # not a palindrome
            if head.val != head_second_half.val:
                break
            head = head.next
            head_second_half = head_second_half.next

        # revert the reverse of the second half to get the original list back
        self.reverse(copy_head_second_half)

        # if both halves match they will be both None
        if head is None or head_second_half is None:
            return True

        return False

    def reverse(self, head):
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev