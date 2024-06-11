# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/656f0374b25e10bfbdc3bb17

'''Problem:
We are given an array people where each element people[i] represents the weight of the i-th person.
There is also a weight limit for each boat. Each boat can carry at most two people at a time,
but the combined weight of these two people must not exceed limit.
The objective is to determine the minimum number of boats required to carry all the people.

Input: people = [10, 55, 70, 20, 90, 85], limit = 100
Output: 4
Explanation: One way to transport all people using 4 boats is as follows:
- Boat 1: Carry people with weights 10 and 90 (total weight = 100).
- Boat 2: Carry a person with weight 85 (total weight = 85).
- Boat 3: Carry people with weights 20 and 70 (total weight = 90).
- Boat 4: Carry people with weights 55 (total weight = 55).
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of people for sorting
# O(1) space
class Solution:
    def numRescueBoats(self, people, limit):
        # sort the list in ascending order
        people.sort()

        # pointer for the lightest person
        i = 0
        # pointer for the heaviest person
        j = len(people) - 1
        # count of boats
        boats = 0

        while i < j:
            if people[i] + people[j] <= limit:
                # if the lightest and heaviest person can share a boat,
                # so move to the next lightest person
                i += 1
            # move to the next heaviest person anyway, because
            # even if we cannot fit two people, we will still fit the heaviest person
            j -= 1

            # increment boat count
            boats += 1

            # it means the last person is left, we need another boat
            if i == j:
                boats += 1

        # return the total number of boats needed
        return boats