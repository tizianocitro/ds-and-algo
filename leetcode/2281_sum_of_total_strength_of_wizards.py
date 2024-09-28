# !code: 2281, !difficulty: hard, !from: https://leetcode.com/problems/sum-of-total-strength-of-wizards/

'''Problem:
As the ruler of a kingdom, you have an army of wizards at your command.
You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard.
For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:
- The strength of the weakest wizard in the group.
- The total of all the individual strengths of the wizards in the group.

Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 10 ** 9 + 7.
A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= strength.length <= 105
- 1 <= strength[i] <= 109

Input: strength = [1,3,1,2]
Output: 44
Explanation: The following are all the contiguous groups of wizards:
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
- [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.

Input: strength = [5,4,6]
Output: 213
Explanation: The following are all the contiguous groups of wizards: 
- [5] from [5,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25
- [4] from [5,4,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16
- [6] from [5,4,6] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36
- [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.
'''

'''Solution:
An example to clarify some of the variables used in the solution:
Suppose strength = [2, 1, 3, 4] and we are evaluating the element strength[1] = 1, then the subarrays
where 1 is the minimum are [1], [2, 1], [1, 3], and [2, 1, 3] (all containing 1 as the minimum).

1. Preprocessing:
- The Left Bound (left_index): This array holds the nearest index to the left where a smaller value exists.
  For strength[1] = 1, the left bound is -1 because there’s no smaller value on the left.
- The Right Bound (right_index): This array holds the nearest index to the right where a smaller value exists.
  For strength[1] = 1, the right bound is n = 4 because no smaller value exists on the right side.
- After running the loops, you get:
    - left_index = [-1, -1, 1, 2] (for index 1, 1 has no smaller element to its left)
	- right_index = [1, 4, 4, 4] (for index 1, 1 has no smaller element to its right, so the right boundary is the end)

2. Compute presum_of_presum, this is the prefix sum of the prefix sum of the strength array.
	1.	Prefix Sum of strength = [2, 1, 3, 4] is prefix_sum = [0, 2, 3, 6, 10] (the first 0 is because of the initial=0).
	2.	Prefix Sum of prefix_sum (i.e., presum_of_presum) is presum_of_presum = [0, 0, 2, 5, 11, 21].

3. Calculate the Contribution for strength[1] = 1:
- left_count refers to how many subarrays can extend to the left where 1 is the minimum (i.e., [1], [2, 1]).
  Since left_index[1] = -1, the count is 1 - (-1) = 2.
- right_count refers to how many subarrays extend to the right (i.e., [1], [1, 3], [1, 3, 4]).
  Since right_index[1] = 4, the count is 4 - 1 = 3.

4. Negative and Positive Prefix Sums:
- neg_presum represents the sum of prefix sums of subarrays ending at strength[1].
- pos_presum represents the sum of prefix sums of subarrays starting at strength[1].
'''

# solution one using prefix sum and monotonic stack
# Complexity:
# O(n) time - where n is the length of the strength array
# O(n) space - where n is the length of the strength array
# (for the left_index, right_index, and presum_of_presum arrays)
from itertools import accumulate

class Solution:
    def totalStrength(self, strength) -> int:
        mod = 10 ** 9 + 7
        n = len(strength)

        # get the first index of the non-larger (smaller or equal) value to strength[i]'s right
        right_index = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                right_index[stack.pop()] = i
            stack.append(i)

        # get the first index of the smaller value to strength[i]'s left
        left_index = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                left_index[stack.pop()] = i
            stack.append(i)

        # prefix sum of the prefix sum array of strength
        # list() because accumulate returns an iterator object which is not subscriptable
        presum_of_presum = list(accumulate(accumulate(strength, initial=0), initial=0))

        result = 0
        # for each element in strength, we get the value of R_term - L_term
        for i in range(n):
            # get the left index and the right bound
            left_bound = left_index[i]
            right_bound = right_index[i]

            # get the left_count and right_count
            # left_count gives the number of valid subarrays where strength[i]
            # is the minimum in subarrays that end at i
            left_count = i - left_bound

            # right_count gives the number of valid subarrays where strength[i]
            # is the minimum in subarrays that start at i
            right_count = right_bound - i

            # get positive presum and the negative presum
            # we modulo it already to avoid overflow
            neg_presum = (presum_of_presum[i + 1] - presum_of_presum[i - left_count + 1]) % mod
            pos_presum = (presum_of_presum[i + right_count + 1] - presum_of_presum[i + 1]) % mod

            # the total strength of all subarrays that have strength[i] as the minimum
            # (pos_presum * left_count - neg_presum * right_count) helps in calculating
            # the net contribution of strength[i] as a minimum in all the relevant subarrays
            result += strength[i] * (pos_presum * left_count - neg_presum * right_count)

            # we modulo the result again to avoid overflow
            result %= mod

        return result