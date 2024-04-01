# !difficulty: hard, !from: https://www.algoexpert.io/questions/quick-sort

# Quick Sort works by picking a "pivot" number from an array,
# positioning every other number in the array in sorted order with respect to the pivot
# (all smaller numbers to the pivot's left; all bigger numbers to the pivot's right),
# and then repeating the same two steps on both sides of the pivot until the entire array is sorted.

# Pick a random number from the input array (the first number, for instance) and let that number be the pivot.
# Iterate through the rest of the array using two pointers,
# one starting at the left extremity of the array and progressively moving to the right,
# and the other one starting at the right extremity of the array and progressively moving to the left.
# As you iterate through the array, compare the left and right pointer numbers to the pivot.
# If the left number is greater than the pivot and the right number is less than the pivot, swap them;
# this will effectively sort these numbers with respect to the pivot at the end of the iteration.
# If the left number is ever less than or equal to the pivot, increment the left pointer;
# similarly, if the right number is ever greater than or equal to the pivot, decrement the right pointer.
# Do this until the pointers pass each other, at which point swapping the pivot with the right number should position the pivot in its final, sorted position,
# where every number to its left is smaller and every number to its right is greater.

# Repeat the process mentioned prviously on the respective subarrays located to the left and right of your pivot,
# and keep on repeating the process thereafter until the input array is fully sorted.

# Complexity
# Best: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Average: O(nlog(n) time | O(log(n)) space - where n is the length of the input array
# Worst: O(n^2) time | O(log(n)) space - where n is the length of the input array (due to bad pivot choice)

# solution one
def quick_sort(array):
    helper(array, 0, len(array) - 1)
    return array

def helper(array, start_index, end_index):
    # stop condition
    if end_index <= start_index:
        return

    # starting with pivot as the first element in the array
    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index

    while right_index >= left_index:
        if array[left_index] > array[pivot_index] and array[right_index] < array[pivot_index]:
            swap(array, left_index, right_index)
        # if they respect these two conditions,
        # the elements are already in the correct position
        if array[left_index] <= array[pivot_index]:
            left_index += 1
        if array[right_index] >= array[pivot_index]:
            right_index -= 1

    # putting the pivot in the sorted position by swapping it with the element at right_index,
    # so right_indix is now the pivot index
    swap(array, pivot_index, right_index)

    # recursive call is made first on the smaller array for space complexity,
    # so that you have at most log(n) calls in the call stack and do not exceed log(n) space complexity
    left_array_length = start_index + (right_index - 1)
    right_array_length = end_index - (right_index + 1)
    is_left_array_smaller = left_array_length < right_array_length
    if is_left_array_smaller:
        helper(array, start_index, right_index - 1)
        helper(array, right_index + 1, end_index)
    else:
        helper(array, right_index + 1, end_index)
        helper(array, start_index, right_index - 1)

def swap(array, left_index, right_index):
    array[left_index], array[right_index] = array[right_index], array[left_index]

# Complexity
# Best: O(nlog(n)) time | O(nlog(n)) space - where n is the length of the input array
# Average: O(nlog(n) time | O(nlog(n)) space - where n is the length of the input array
# Worst: O(n^2) time | O(nlog(n)) space - where n is the length of the input array (due to bad pivot choice)

# space is because we create array of space O(n) each of the log(n) calls.

# solution two
def quickSort(array):
    # stop condition
    if len(array) <= 1:
        return array

    # gets and removes the last element in an array
    pivot = array.pop()
    left_array = []
    right_array = []

    for i in range(len(array)):
        if array[i] < pivot:
            left_array.append(array[i])
        else:
            right_array.append(array[i])

    # recursively on the other two arrays
    return quickSort(left_array) + [pivot] + quickSort(right_array)