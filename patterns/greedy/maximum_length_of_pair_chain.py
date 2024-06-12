# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6570659b3d4f8073f08461c9

'''Problem:
Given a collection of pairs where each pair contains two elements [a, b], find the maximum length of a chain you can form using pairs.
A pair [a, b] can follow another pair [c, d] in the chain if b < c.
You can select pairs in any order and don't need to use all the given pairs.

Input: [[1,2], [3,4], [2,3]]
Expected Output: 2
Explaination: The longest chain is [1,2] -> [3,4]. The chain [1,2] -> [2,3] is invalid because 2 is not smaller than 2.

Input: [[5,6], [1,2], [8,9], [2,3]]
Expected Output: 3
Explaination: The chain can be [1,2] -> [5,6] -> [8,9] or [2,3] -> [5,6] -> [8, 9].

Input: [[7,8], [5,6], [1,2], [3,5], [4,5], [2,3]]
Expected Output: 3
Explaination: The longest possible chain is formed by chaining [1,2] -> [3,5] -> [7,8].
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of pairs because of sorting
# O(1) space
class Solution:
    def findLongestChain(self, pairs):
        if len(pairs) < 1:
            return 0

        # we need to sort by end of interval because
        # we want to start with the interval that finishes first
        pairs.sort(key=lambda x: x[1])

        prev_end = pairs[0][1]
        chain_len = 1

        # iterate through the pairs starting from the second one and check
        # if the start of the current pair is greater than the end of the previous pair
        # if it is, we can add it to the chain
        for i in range(1, len(pairs)):
            start, end = pairs[i]
            if start > prev_end:
                prev_end = end
                chain_len += 1

        return chain_len

# solution two
# Complexity:
# O(nlogn) time - where n is the number of pairs because of sorting
# O(1) space
class Solution:
    def findLongestChain(self, pairs):
        # sort pairs based on their second element in ascending order
        pairs.sort(key=lambda x: x[1])

        prev_end = float('-inf')
        chain_len = 0

        for pair in pairs:
            # check if the first element of the pair is greater than the current end
            if pair[0] > prev_end:
                # update the current end and increment the chain count
                prev_end = pair[1]
                chain_len += 1

        return chain_len