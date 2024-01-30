# !difficulty: hard

''' Problem:
We are given an array containing positive and negative numbers.
Suppose the array contains a number M at a particular index.
Now, if M is positive we will move forward M indices and if M is negative move backwards M indices.
You should assume that the array is circular which means two things:
1. If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
2. If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.

Write a method to determine if the array has a cycle.
The cycle should have more than one element and should follow one direction
which means the cycle should not contain both forward and backward movements.

Input: [1, 2, -1, 2, 2]
Output: true
Explanation: the array has a cycle among indices: 0 -> 1 -> 3 -> 0

Input: [2, 2, -1, 2]
Output: true
Explanation: the array has a cycle among indices: 1 -> 3 -> 1

Input: [2, 1, -1, -2]
Output: false
Explanation: the array does not have any cycle
'''

# solution one
# Complexity:
# O(n^2) time - where n is the number of elements in the array
# This is due to the fact that we are iterating all elements and trying to find a cycle for each element.
# O(1) space
class Solution:
    def loopExists(self, arr):
        # iterat through the all elements of the array because
        # if a number does not have a cycle we have to move forward to check the next element
        for i in range(len(arr)):
            # if we are moving forward or not
            direction = arr[i] >= 0
            slow, fast = i, i

            # if slow or fast becomes -1 this means we can't find cycle for this number
            while slow != -1 or fast != -1:
                # move one step for slow pointer
                slow = self.findNextIndex(arr, slow, direction)
                # move one step for fast pointer
                fast = self.findNextIndex(arr, fast, direction)
                if fast != -1:
                    # move another step for fast pointer
                    fast = self.findNextIndex(arr, fast, direction)
                if slow == fast:
                    break

            if slow != -1 and fast != -1 and slow == fast:
                return True

        return False

    def findNextIndex(self, arr, currentIndex, direction):
        elDirection = arr[currentIndex] >= 0

        # change in direction, return -1
        if elDirection != direction:
            return -1
        
        nextIndex = (currentIndex + arr[currentIndex]) % len(arr)

        # one element cycle, return -1
        if nextIndex == currentIndex:
            return -1
        
        return nextIndex

# solution two
'''
In solution one, we don’t keep a record of all the numbers that have been evaluated for cycles.
We know that all such numbers will not produce a cycle for any other instance as well.
If we can remember all the numbers that have been visited, our algorithm will improve to O(n) time as, then, each number will be evaluated for cycles only once.
We can keep track of this by creating a separate array, however, in this case, the space complexity of our algorithm will increase to O(n).
'''
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(n) space - where n is the number of elements in the array
class Solution:
    def loopExists(self, arr):
        for i in range(len(arr)):
            # if we are moving forward or not
            direction = arr[i] >= 0
            slow, fast = i, i
            seen = set([i])

        while True:
            # move one step for slow pointer
            slow = self.findNextIndex(arr, slow, direction)
            # move one step for fast pointer
            fast = self.findNextIndex(arr, fast, direction)
            if fast != -1:
                # move another step for fast pointer
                fast = self.findNextIndex(arr, fast, direction)
            if slow in seen or fast in seen or slow == -1 or fast == -1:
                break
            seen.add(slow)
            seen.add(fast)

        if slow != -1 and (slow in seen or fast in seen):
            return True

        return False

    def findNextIndex(self, arr, currentIndex, direction):
        elDirection = arr[currentIndex] >= 0

        # change in direction, return -1
        if elDirection != direction:
            return -1

        nextIndex = (currentIndex + arr[currentIndex]) % len(arr)

        # one element cycle, return -1
        if nextIndex == currentIndex:
            return -1

        return nextIndex