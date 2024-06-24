# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/65733882c593a75ac0c3316a

'''Problem:
Determine the minimum number of deletions required to remove the smallest and the largest elements from an array of integers.

In each deletion, you are allowed to remove either the first (leftmost) or the last (rightmost) element of the array.

Input: [3, 2, 5, 1, 4]
Output: 3
Explanation: The smallest element is 1 and the largest is 5. Removing 4, 1, and then 5 (or 5, 4, and then 1) in three moves is the most efficient strategy.

Input: [7, 5, 6, 8, 1]
Output: 2
Explanation: Here, 1 is the smallest, and 8 is the largest. Removing 1 and then 8 in two moves is the optimal strategy.

Input: [2, 4, 10, 1, 3, 5]
Output: 4
Explanation: The smallest is 1 and the largest is 10. One strategy is to remove 2, 4, 10, and then 1 in four moves.
'''

# solution one
# O(n) time - where n is the length of the input list
# O(1) space
class Solution:
    def minMoves(self, nums):
        left_both, left_min, left_max = 0, 0, 0
        right_both, right_min, right_max = 0, 0, 0
        min_num, max_num = float('inf'), float('-inf')

        left, right = 0, len(nums) - 1
        deletions_count = 1

        while left < len(nums):
            left_num, right_num = nums[left], nums[right]

            # update the min and max numbers for the next part to work
            min_num = min(min_num, min(left_num, right_num))
            max_num = max(max_num, max(left_num, right_num))

            # whenever we find the min or max number, we update the deletions count
            # the *_both keeps track of the last deletions count when we found the min or max number
            # because it will be the second number between the min and max number to delete,
            # so in case they are both at the same end, we can use the last deletions count
            # the *_min and *_max are used for when we delete one per each end
            if left_num == min_num:
                left_both = left_min = deletions_count
            if left_num == max_num:
                left_both = left_max = deletions_count

            if right_num == min_num:
                right_both = right_min = deletions_count
            if right_num == max_num:
                right_both = right_max = deletions_count

            deletions_count += 1
            left += 1
            right -= 1

        return min(
            min(left_min + right_max, right_min + left_max), # one from each end
            min(left_both, right_both) # both from one end, either left or right
        )

# solution two
# O(n) time - where n is the length of the input list
# O(1) space
class Solution:
    def minMoves(self, nums):
        n = len(nums)

        # find the indexes of the minimum and maximum elements
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # calculate distances from both ends
        min_dist_start = min_index + 1
        min_dist_end = n - min_index
        max_dist_start = max_index + 1
        max_dist_end = n - max_index

        # determine the most efficient sequence of moves
        total_moves = min(
            max(min_dist_start, max_dist_start), # both from start
            min(min_dist_start + max_dist_end, min_dist_end + max_dist_start), # one from each end
            max(min_dist_end, max_dist_end) # both from end
        )

        return total_moves