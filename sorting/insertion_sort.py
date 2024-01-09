# !difficulty: easy

# Divide the input array into two subarrays in place.
# The first subarray should be sorted at all times and should start with a length of 1, while the second subarray should be unsorted.
# Iterate through the unsorted subarray, inserting all of its elements into the sorted subarray in the correct position by swapping them into place.
# Eventually, the entire array will be sorted.

# Complexity
# Best: O(n) time | O(1) space - where n is the length of the input array
# Average: O(n^2) time | O(1) space - where n is the length of the input array
# Worst: O(n^2) time | O(1) space - where n is the length of the input array

# solution one
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] >= array[j - 1]:
                break
            array[j], array[j - 1] = array[j - 1], array[j]
    return array

# solution two
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j] <= array[i]:
                break
            array[j], array[i] = array[i], array[j]
            i -= 1
    return array