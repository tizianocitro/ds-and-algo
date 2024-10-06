# !code: 875, !difficulty: medium, !from: https://leetcode.com/problems/koko-eating-bananas/

'''Problem:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Input: piles = [30,11,23,4,20], h = 6
Output: 23
'''

# solution one using binary search
# Complexity:
# O(nlogm) time - where n is the length of piles and m is max(piles)
# O(1) space
import math

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        # right is max(piles) because you cannot eat more bananas
        # than the ones in the biggest pile
        left, right = 1, max(piles)

        while left < right:
            # get the middle index between left and right boundary indexes,
            # the middle will be the current speed for koko to eat bananas
            speed = (left + right) // 2

            # iterate over the piles and calculate hour_spent,
            # we increase the hour_spent by ceiling pile / middle
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / speed)

            # check if the current speed is a workable speed,
            # and cut the search space by half
            if hours_spent <= h:
                right = speed
            else:
                left = speed + 1

        # once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed, so we could return left as well
        return right



