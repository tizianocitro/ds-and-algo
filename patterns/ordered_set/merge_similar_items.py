# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/merge-similar-items-easy

'''Problem:
Given two 2D arrays of item-value pairs, named items1 and items2, where item[i] = [valuei, weighti]
and each valuei in these arrays is unique within its own array and is paired with a weighti.

Combine these arrays such that if a value appears in both, its weights are summed up.
The final merged array should be sorted based on the valuei.

Input: items1 = [[1,2],[4,3]], items2 = [[2,1],[4,3],[3,4]]
Output: [[1,2],[2,1],[3,4],[4,6]]
Explanation: Item 1 has value 2 in items1 and doesn't exist in items2, item 2 has value 1 in items2, item 4 is summed up.

Input: items1 = [[5,5]], items2 = [[5,10]]
Output: [[5,15]]
Explanation: Item 5 exists in both arrays, so their values are summed.

Input: items1 = [[1,1],[2,2]], items2 = [[3,3]]
Output: [[1,1],[2,2],[3,3]]
Explanation: All items are unique across items1 and items2, so they remain unchanged.
'''

# solution one
# Complexity:
# O(nlogn) time - for sorting, where n is the total number of items in both lists
# O(n) space - for the merged_items dictionary
class Solution:
    def mergeSimilarItems(self, items1, items2):
        merged_items = {}
        for item, value in items1:
            merged_items[item] = merged_items.get(item, 0) + value
        for item, value in items2:
            merged_items[item] = merged_items.get(item, 0) + value

        # sort and return the result based on item id,
        # we need to sort because dictionaries preserve insertion order
        # and not the order of the items by the keys
        return sorted([[item, value] for item, value in merged_items.items()])

# solution two using defaultdict
# Complexity:
# O(nlogn) time - for sorting, where n is the total number of items in both lists
# O(n) space - for the merged_items dictionary
from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1, items2):
        # using defaultdict to automatically handle non-existing keys
        merged_items = defaultdict(int)

        # process items from the first list
        for item, value in items1:
            merged_items[item] += value

        # process items from the second list
        for item, value in items2:
            merged_items[item] += value

        # sort and return the result based on item id
        return sorted([[item, value] for item, value in merged_items.items()])