# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639ddbfd1558f46adcdc699c

# solution one
# Complexity:
# O(n * 2^n) time - where n is the total number of nodes in the tree
# O(2^n) space - where n is the total number of nodes in the tree
class Solution:
    def countTrees(self, n):
        return self.countTreesRecursive(1, n)

    def countTreesRecursive(self, start, end):
        if start > end:
            # the one counts as a leaf node [Node]
            # returning 0 here would lead to a loss in 
            return 1

        count = 0
        for i in range(start, end + 1):
            left_count = self.countTreesRecursive(start, i - 1)
            right_count = self.countTreesRecursive(i + 1, end)
            count += left_count * right_count

        return count

# solution two is a better version of solution one with memoization
# Complexity:
# O(n^2) time - where n is the total number of nodes in the tree
# because we iterate from ‘1’ to ‘n’ and ensure that each sub-problem is evaluated only once
# O(n) space - where n is the total number of nodes in the tree for the for the memoization map
class Solution:
    def countTrees(self, n):
        return self.countTreesRecursive(1, n, {})

    def countTreesRecursive(self, start, end, map):
        key = f'{start}-{end}'
        if key in map:
            return map[key]

        if start > end:
            # the one counts as a leaf node [Node]
            # returning 0 here would lead to a loss in 
            return 1

        count = 0
        for i in range(start, end + 1):
            left_count = self.countTreesRecursive(start, i - 1, map)
            right_count = self.countTreesRecursive(i + 1, end, map)
            count += left_count * right_count

        map[key] = count

        return count

# solution three
# Complexity:
# O(n * 2^n) time - where n is the total number of nodes in the tree
# O(2^n) space - where n is the total number of nodes in the tree
class Solution:
    def countTrees(self, n):
        if n <= 1:
            return 1

        count = 0
        for i in range(1, n + 1):
            # making 'i' root of the tree
            left_count = self.countTrees(i - 1)
            right_count = self.countTrees(n - i)
            count += left_count * right_count

        return count

# solution four is a better version of solution three with memoization
# Complexity:
# O(n^2) time - where n is the total number of nodes in the tree
# because we iterate from ‘1’ to ‘n’ and ensure that each sub-problem is evaluated only once
# O(n) space - where n is the total number of nodes in the tree for the for the memoization map
class Solution:
    def countTrees(self, n):
        return self.countTreesMemoized(n, {})

    def countTreesMemoized(self, n, map):
        if n in map:
            return map[n]

        if n <= 1:
            return 1

        count = 0
        for i in range(1, n + 1):
            # making 'i' root of the tree
            countOfLeftSubtrees = self.countTreesMemoized(i - 1, map)
            countOfRightSubtrees = self.countTreesMemoized(n - i, map)
            count += countOfLeftSubtrees * countOfRightSubtrees

        map[n] = count

        return count