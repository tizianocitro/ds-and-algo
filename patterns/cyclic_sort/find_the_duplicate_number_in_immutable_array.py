# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd9431488110f74a921e1a

'''Problem:
We are given an unsorted array containing n + 1 numbers taken from the range 1 to n.
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space and without modifying the input array.

Input: [1, 4, 4, 3, 2]
Output: 4
'''

'''Solution:
While doing the cyclic sort, we realized that the array will have a cycle due to the duplicate number
and that the start of the cycle will always point to the duplicate number.
This means that we can use the fast & the slow pointer method to find the duplicate number
or the start of the cycle similar to Start of LinkedList Cycle.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findDuplicate(self, arr):
        # the fast pointer here moves twice as fast as the slow pointer
        # in a sense that it moves by using the value of the current element
        # as the index for the next step
        slow, fast = arr[0], arr[arr[0]]
        while slow != fast:
            slow = arr[slow]
            fast = arr[arr[fast]]

        # find cycle length
        current = arr[arr[slow]]
        cycleLength = 1
        while current != arr[slow]:
            current = arr[current]
            cycleLength += 1

        return self.find_start(arr, cycleLength)


    def find_start(self, arr, cycleLength):
        pointer1, pointer2 = arr[0], arr[0]

        # move pointer2 ahead 'cycleLength' steps
        while cycleLength > 0:
            pointer2 = arr[pointer2]
            cycleLength -= 1

        # increment both pointers until they meet at the start of the cycle
        while pointer1 != pointer2:
            pointer1 = arr[pointer1]
            pointer2 = arr[pointer2]

        return pointer1