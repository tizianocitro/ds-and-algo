# Write a function that takes in an array of integers and returns the length of the longest peak in the array.
# A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak),
# at which point they become strictly decreasing.
# At least three integers are required to form a peak.
# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0.
# Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.

# Input: array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# Output: 6 because we have [0, 10, 6, 5, -1, -3]

# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space

# solution one
def longestPeak(array):
    longest = 0
    i = 1
    while i < len(array) - 1:
        peak = array[i]
        isPeak = peak > array[i - 1] and peak > array[i + 1]
        if not isPeak:
            i += 1
            continue

        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1
        
        current = right - left - 1
        longest = max(longest, current)
        i = right
        
    return longest

# solution two
def longestPeak(array):
    longest = 0
    temp_length = 1
    is_increasing = False
    is_decreasing = False
    for idx in range(1, len(array)):
        if array[idx] > array[idx-1] and is_decreasing is False:
            temp_length += 1
            is_increasing = True
        elif array[idx] < array[idx-1] and is_increasing is True:
            temp_length += 1
            is_decreasing = True
            longest = max(longest, temp_length)
        elif array[idx] == array[idx-1]:
            temp_length = 1
            is_decreasing = False
            is_increasing = False
        elif array[idx] > array[idx-1] and is_decreasing is True:
            temp_length = 2
            is_decreasing = False
            is_increasing = True
    return longest