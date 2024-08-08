# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6385d2dae25dea6343fd8b19

'''Problem:
You are visiting a farm to collect fruits. The farm has a single row of fruit trees.
You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree.
The farm has following restrictions:
1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
2. You can start with any tree, but you can’t skip a tree once you have started.
3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Input: fruit = ['A', 'B', 'C', 'A', 'C']  
Output: 3  
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']  
Output: 5  
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

# solution one
# Complexity:
# O(n) time - where n is the number of elements in the input list
# O(1) space - because it is O(k) where k is the number of unique elements,
# for this problem k = 2, so O(1) space
class Solution:
    def findLength(self, fruits):
        max_length = 0
        fruit_frequencies = {}
        start = 0

        for end in range(len(fruits)):
            fruit = fruits[end]
            fruit_frequencies[fruit] = fruit_frequencies.get(fruit, 0) + 1

            # 2 because we have two baskets
            while len(fruit_frequencies) > 2:
                fruit = fruits[start]
                fruit_frequencies[fruit] -= 1
                if fruit_frequencies[fruit] <= 0:
                    del fruit_frequencies[fruit]
                start += 1

            # in this case you need to do it here otherwise the solution won't work
            max_length = max(max_length, end - start + 1)
        return max_length
