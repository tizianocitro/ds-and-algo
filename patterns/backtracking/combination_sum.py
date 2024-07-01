# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63d3bfa4f81b8e2fe5ded9c4

'''Problem:
Given an array of distinct positive integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Input: candidates = [2, 3, 6, 7], target = 7  
Output: [[2, 2, 3], [7]]  
Explanation: The elements in these two combinations sum up to 7.

Input: candidates = [2, 4, 6, 8], target = 10  
Output: [[2,2,2,2,2], [2,2,2,4], [2,2,6], [2,4,4], [2,8], [4,6]]    
Explanation: The elements in these six combinations sum up to 10.
'''

'''Solution:
Let’s try this approach on the following input: Candidates: [3, 4, 5], Target: 9.
Here are the number of steps in our algorithm:

1. We will start with an empty set. This also means that the sum of the elements in the set is zero.
2. We can try adding all three numbers separately in the set. This will give us three sets: [3], [4], [5].
3. Let’s take set [3], since the sum of its elements is less than the Target (=9), we will try adding more numbers to it.
4. We can add all three numbers again to generate new sets. We can add '3’ again, as each number can be added multiple times.
5. After adding all numbers separately to the set [3], we will get the following sets: [3, 3], [3, 4], [3, 5]. We can see, each set has a sum less than the target.
6. We can now, repeat the same process as described in step-4.
    6.1. For [3, 3]: Adding '3’ will give us a valid solution [3, 3, 3] having a sum equal to the target. Adding '4’ and '5’ will give us a sum which is greater than the target. Therefore, we can stop the search here for this set, as adding any additional number will not produce a correct solution.
    6.2. For [3, 4]: We will add '4’ or '5’ to it, which will give us a sum greater than the target. We will stop our search here for this set.
    6.3. For [3, 5]: We can only add '5’ to it, which does not produce a valid solution.
7. Similar approach can be applied to other sets.

In the end, we can see that the valid solutions are: [3, 3, 3] and [4, 5].
'''

# solution one
# Complexity:
# O(n^t/m+1) time - where n is the number of candidates, t is the target value, and m is the minimum value among the candidates
# This is because the execution of the backtracking is similar to a DFS traversal of an n-ary tree. So, the time complexity would be the same as the number of nodes in the n-ary tree.
# Each node can call the backtrack function a maximum of n times, i.e., the total number of candidates.
# The maximal depth of the n-ary tree would be t/m, where we keep on adding the smallest element to the combination.
# As we know, the maximal number of nodes in n-ary tree of t/m height would be n^t/m+1, hence the time complexity is O(n^t/m+1).
# O(t/m) space - where t is the target value and m is the minimum value among the candidates
# Ignoring the space needed for the output array, the space complexity would be O(t/m) because at any time, we can pile up to t/m recursive calls of the backtrack function,
# this will happen when we keep on adding the smallest element to the combination. As a result, the space overhead of the recursion is O(t/m).
class Solution:
    def combinationSum(self, candidates, target):
        # store the final result
        result = []
        self.backtrackCombinationSum(candidates, target, 0, [], result)
        return result

    def backtrackCombinationSum(self, candidates, target, start, comb, result):
        # if target is 0, we have found a valid combination
        if target == 0:
            # append a copy of the current combination to the result list
            # we need a copy because otherwise it would be updated (reference-passing)
            result.append(list(comb))
            return

        # this can be done in alternative to doing it
        # in the if candidate > target during the loop
        # if target < 0:
        #   return

        # iterate through the candidates array starting from the given start index
        # for each number start form the current number to all the next ones
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            # if the current candidate is greater than the remaining target, move on to the next
            if candidate > target:
                continue
            
            # add the current candidate to the current combination
            comb.append(candidate)

            # recursively call the function with the updated combination and remaining target
            self.backtrackCombinationSum(candidates, target - candidate, i, comb, result)

            # backtrack by removing the last added candidate from the combination
            comb.pop()

# solution two
# Complexity:
# O(2^n * t/m) time - where n is the number of candidates
# The 2^n is because for each candidate, we have two choices, either to include it in the combination or not.
# O(n * t/m) space - where n is the number of candidates
class Solution:
    def combinationSum(self, candidates, target):
        # store the final result
        result = []
        self.backtrackCombinationSum(candidates, target, 0, [], result)
        return result

    def backtrackCombinationSum(self, candidates, target, current_index, comb, result):
        # if target is 0, we have found a valid combination
        if target == 0:
            # append a copy of the current combination to the result list
            # we need a copy because otherwise it would be updated (reference-passing)
            result.append(list(comb))
            return

        # if we exceed the target or we have no more candidates
        if target < 0 or current_index >= len(candidates):
            return

        candidate = candidates[current_index]

        # include the current candidate in the combination
        comb.append(candidate)
        # recursive call including the current candidate in the combination
        self.backtrackCombinationSum(candidates, target - candidate, current_index, comb, result)
        # remove the current candidate in the combination
        comb.pop()

        # recursive call without including the current candidate in the combination
        self.backtrackCombinationSum(candidates, target, current_index + 1, comb, result)