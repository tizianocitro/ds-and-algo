# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd75e8b9c2c77f772df326

'''Problem:
Given a binary tree and a number S, find all paths in the tree such that the sum of all the node values of each path equals S.
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

Input: [1, 7, 9, 6, 5, 2, 3], S = 12
Output: 3
Explanation: There are three paths with sum 12: 7 -> 5, 1 -> 9 -> 2, and 9 -> 3.
'''

# solution one with count as parameter
# Complexity:
# O(nlogn) time - where n is the number of nodes in the tree
# the complexity is O(n) beause we traverse all nodes in the tree
# and for each node we traverse all nodes in the path to the node, which takes O(n)
# so the complexity should be O(n^2) but the length of a path is equal to the height of the tree,
# which in a balanced tree is logn, so the complexity is O(nlogn). The same worst case happens also in non-balanced trees
# O(n) space - where n is the number of nodes in the tree because of the recursion stack and the path list
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPaths(self, root, s):
        count = 0
        return self.dfsCount(root, s, count, [])
    
    def dfsCount(self, root, s, count, path):
        if root is None:
            return count

        path.append(root.val)

        val = 0
        for n in reversed(path):
            val += n
            if val == s:
                count += 1
                break

        # this if could be avoided because we are already checking if root is None
        # so if we pass the the left and right of a leave, the call will have root as None
        # so it will stop at the first check
        if root.left is not None or root.right is not None:
            count = self.dfsCount(root.left, s, count, path)
            count = self.dfsCount(root.right, s, count, path)

        del path[-1]

        return count

# solution two without count as parameter
# Complexity:
# O(nlogn) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree because of the recursion stack and the path list
# explanation is the same as the first solution
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPaths(self, root, s):
        return self.dfsCount(root, s, [])
    
    def dfsCount(self, root, s, path):
        if root is None:
            return 0

        path.append(root.val)

        count, val = 0, 0
        for n in reversed(path):
            val += n
            if val == s:
                count += 1
                break

        # this if could be avoided because we are already checking if root is None
        # so if we pass the the left and right of a leave, the call will have root as None
        # so it will stop at the first check
        if root.left is not None or root.right is not None:
            count += self.dfsCount(root.left, s, path)
            count += self.dfsCount(root.right, s, path)

        del path[-1]

        return count

'''A more efficient solution:
One thing we are repeating for each node is traversing the current path and seeing if any sub-path that ends at the current node gives us the required sum.
We can use the Prefix Sum technique to efficiently manage the path sums.

Prefix Sum
Let’s first understand what Prefix Sum is. For a given array, its Prefix Sum is another array where each element
is the commutative sum of the corresponding element in the given array and all its previous elements.
Input: [1, 6, 2, 5], Prefix Sum: [1, 7, 9, 14]

Now, let’s say we want to find all subarrays of a given array with a target sum.
Let’s say our target sum is 7, and we want to find all the subarrays of the array mentioned above.
We can clearly see that there are two such subarrays: 1) [1, 6], and 2) [2, 5].

How can we utilize the Prefix Sum array to find these two subarrays efficiently?
There are two ways Prefix Sum can help us:

a) Since each element of the prefix sum array contains the cumulative sum of current and previous elements,
   therefore, whenever we see our target sum, we have found our targeted subarray. For example, since the second element of the prefix sum array is 7;
   therefore, our target subarray will be from the start of the array till the second element, i.e., [1, 6]
b) the prefix sum array can also help us find our target subarray that is not starting from the first index.

If we subtract the target sum from any element of the prefix sum array,
the result will also give us our target subarray (if that result is present in the prefix sum array).
For example, take the 4th element of the prefix sum array and subtract the target sum from it: 14 - 7 => 7

Is this result (7) present in the prefix sum array? Yes, it is the second element.
This means the sum from the 3rd element to the current element (i.e., the 4th) is also 7.
Hence, our target subarray will be from the 3rd element to the current element, i.e., [2, 5].

To the original problem, we can consider each path as an array and calculate its prefix sums to find any required sub-paths. 
'''

# solution with prefix sum
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree because of the recursion stack and the map
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def count_paths(self, root, target_sum):
        # A map that stores the number of times a prefix sum has occurred so far.
        map = {}
        return self.count_paths_prefix_sum(root, target_sum, map, 0)

    def count_paths_prefix_sum(self, current_node, target_sum, map, current_path_sum):
        if current_node is None:
            return 0

        # The number of paths that have the required sum.
        path_count = 0

        # 'current_path_sum' is the prefix sum, i.e., sum of all node values from the root 
        # to the current node.
        current_path_sum += current_node.val

        # This is the base case. If the current sum is equal to the target sum, we have found 
        # a path from root to the current node having the required sum. Hence, we increment 
        # the path count by 1.
        if target_sum == current_path_sum:
            path_count += 1

        # 'current_path_sum' is the path sum from root to the current node. If within this path, 
        # there is a valid solution, then there must be an 'old_path_sum' such that:
        # => current_path_sum - old_path_sum = target_sum
        # => current_path_sum - target_sum = old_path_sum
        # Hence, we can search such an 'old_path_sum' in the map from the key 
        # 'current_path_sum - target_sum'.
        path_count += map.get(current_path_sum - target_sum, 0)

        # This is the key step in the algorithm. We are storing the number of times the prefix sum
        # `current_path_sum` has occurred so far.
        # it can become higher than one if one of the node in the path has val == 0
        map[current_path_sum] = map.get(current_path_sum, 0) + 1

        # Counting the number of paths from the left and right subtrees.
        path_count += self.count_paths_prefix_sum(current_node.left, target_sum, map, current_path_sum)
        path_count += self.count_paths_prefix_sum(current_node.right, target_sum, map, current_path_sum)

        # Removing the current path sum from the map for backtracking.
        # 'current_path_sum' is the prefix sum up to the current node. When we go 
        # back (i.e., backtrack), then the current node is no more a part of the path, hence, we 
        # should remove its prefix sum from the map.
        map[current_path_sum] = map.get(current_path_sum, 1) - 1

        return path_count
