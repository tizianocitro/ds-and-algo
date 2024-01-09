# !difficulty: easy

# Divide the input array into two subarrays in place. 
# The first subarray should be sorted at all times and should start with a length of 0, while the second subarray should be unsorted.
# Find the smallest (or largest) element in the unsorted subarray and insert it into the sorted subarray with a swap. 
# Repeat this process of finding the smallest (or largest) element in the unsorted subarray
# and inserting it in its correct position in the sorted subarray with a swap until the entire array is sorted.

# Complexity
# Best: O(n^2) time | O(1) space - where n is the length of the input array
# Average: O(n^2) time | O(1) space - where n is the length of the input array
# Worst: O(n^2) time | O(1) space - where n is the length of the input array

# solution one
def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if array[j] < array[min_index]:
                min_index = j
        if min_index is not i:
            array[i], array[min_index] = array[min_index], array[i]
    return array

# solution two, just using != instead of is not
def selection_sort(array):
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i, length):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array