# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63948df2f34bef51e103b6d7

'''Problem:
Given an unsorted array containing numbers and a number k, find the first k missing positive numbers in the array.

Input: nums = [3, -1, 4, 5, 5], k = 3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Input: nums = [2, 3, 4], k = 3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.
'''

# solution one storing misplaced numbers
# Complexity:
# O(n + k) time - where n is the length of the nums list and k is the number of missing numbers to find
# O(n) space - for the misplacedNumbers set
class Solution:
    def findNumbers(self, nums, k):
        missingNumbers = []
        i = 0
        n = len(nums)

        while i < n:
            num = nums[i]
            j = num - 1
            if num >= 0 and num <= n and num != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                continue
            i += 1

        # any of the additional numbers we have to add if len(missingNumbers) < k
        # could be already part of the array, so we store them to check this later
        misplacedNumbers = set()
        for i in range(n):
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)
                misplacedNumbers.add(nums[i])
                if len(missingNumbers) == k:
                    return missingNumbers

        candidateNumber = n + 1
        while len(missingNumbers) < k:
            if candidateNumber not in misplacedNumbers:
                missingNumbers.append(candidateNumber)
            candidateNumber += 1

        return missingNumbers


# solution two without storing misplaced numbers
# Complexity:
# O(n + k) time - where n is the length of the nums list and k is the number of missing numbers to find
# O(n) space - for the missingNumbers list
class Solution:
    def findNumbers(self, nums, k):
        missingNumbers = []
        i = 0
        n = len(nums)

        while i < n:
            num = nums[i]
            j = num - 1
            if num >= 0 and num <= n and num != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                continue
            i += 1

        for i in range(n):
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)
                if len(missingNumbers) == k:
                    return missingNumbers

        currentlyMissing = len(missingNumbers)
        candidateNumber = n + 1
        # the overall complexity of this while loop is approximately O(k)
        # this will run k - currentlyMissing times
        while len(missingNumbers) < k:
            i = 0
            # if currentlyMissing == 0, this will not run
            # if currentlyMissing > 0, this will run currentlyMissing times
            while i < currentlyMissing:
                missingNumber = missingNumbers[i]
                if nums[missingNumber - 1] == candidateNumber:
                    break
                i += 1

            if i >= currentlyMissing:
                missingNumbers.append(candidateNumber)
            candidateNumber += 1

        return missingNumbers
