# !difficulty: medium

# You're given an unordered list of unique integers nums in the range [1, n], where n represents the length of nums + 2.
# This means that two numbers in this range are missing from the list.
# Write a function that takes in this list and returns a new list with the two missing numbers, sorted numerically.

# Input: [1, 4, 3]
# Output: [2, 5] // n is 5 meaning the complete list of nums is [1, 2, 3, 4, 5]

# solution one
# Complexity:
# O(nlog(n)) time - because of sorting
# O(n) space - because of the missingNums array
def missingNumbers(nums):
    if len(nums) < 1:
        return [1, 2]
    
    missingNums = []
    nums.sort()
    
    for i in range(len(nums)):
        n = nums[i]
        if i == 0 and n != 1:
            for j in range(1, n):
                missingNums.append(j)
            continue
        for j in range(nums[i - 1] + 1, n):
            missingNums.append(j)

    highest = nums[len(nums) - 1]
    while len(missingNums) < 2:
        highest += 1
        missingNums.append(highest)
    
    return missingNums
    
# solution two using set
# Complexity:
# O(n) time - where n is the length of nums
# O(n) space - because of the missingNums array and currentNums set
def missingNumbers(nums):
    currentNums = set(nums)
    missingNums = []
    for i in range(1, len(nums) + 3):
        if i not in currentNums:
            missingNums.append(i)
    return missingNums

# solution three using math
# Complexity:
# O(n) time - where n is the length of nums
# O(1) space
def missingNumbers (nums):
    total = sum(range(1, len(nums) + 3))
    for num in nums:
        total -= num
    
    averageMissingValue = total // 2
    foundFirstHalf = 0
    foundSecondHalf = 0
    
    for num in nums:
        if num <= averageMissingValue:
            foundFirstHalf += num
        else:
            foundSecondHalf += num
        
    expectedFirstHalf = sum(range(1, averageMissingValue + 1))
    expectedSecondHalf = sum(range(averageMissingValue + 1, len(nums) + 3))
    
    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]