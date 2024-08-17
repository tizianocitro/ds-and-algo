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

# solution one
# Complexity
# Best: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Average: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Worst: O(n^2) time | O(log(n)) space - where n is the length of the input array (due to bad pivot choice)
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

# solution two
# Complexity
# Best: O(nlog(n)) time | O(nlog(n)) space - where n is the length of the input array
# Average: O(nlog(n)) time | O(nlog(n)) space - where n is the length of the input array
# Worst: O(n^2) time | O(nlog(n)) space - where n is the length of the input array (due to bad pivot choice)
# space is because we create array of space O(n) each of the log(n) calls.
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

# solution three
# Best: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Average: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Worst: O(n^2) time | O(n) space - where n is the length of the input array
# the worst case time complexity happens when the input array is sorted or if all of its elements are the same
def quickSort(array):
    helper(array, 0, len(array) - 1)
    return array

def helper(arr, low, high):
    if low < high:
        # partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # recursively sort the left part of the array
        helper(arr, low, pivot_index - 1)

        # recursively sort the right part of the array
        helper(arr, pivot_index + 1, high)

def partition(arr, low, high):
    if low == high:
        return low

    # here you can also randomly choose the pivot, it greatly reduces
    # the chance of worst case, improving performance on average
    # pick a random pivot and then swap it with the last element
    # so that the code remains the same as the usual partition scheme
    # where the pivot is the last element (index 'high')
    # import random
    # pivot_index = random.randint(low, high)
    # nums[pivot_index], nums[high] = nums[high], nums[pivot_index]

    # choose the last element as the pivot
    pivot = arr[high]
    for i in range(low, high):
        # all elements less than 'pivot' will be before the index 'low'
        if arr[i] < pivot:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1

    # puts the pivot element in its correct sorted position
    arr[low], arr[high] = arr[high], arr[low]

    # return the index of the pivot
    return low

'''Solution (known as Median of Medians):
Median of Medians algorithm allows us to choose a good pivot for the partitioning algorithm of the Quicksort. This algorithm finds an
approximate median of an array in linear time O(n). When this approximate median is used as the pivot, the worst-case complexity of the
partitioning procedure reduces to linear O(n), which is also the asymptotically optimal worst-case complexity of any sorting/selection algorithm.
This algorithm was originally developed by Blum, Floyd, Pratt, Rivest, and Tarjan and was describe in their 1973 paper.

This is how the selction of the pivot using the Median of Medians algorithm works:
- If we have 5 or less than 5 elements in the input array, we simply take its first element as the pivot.
  If not then we divide the input array into subarrays of five elements (for simplicity we can ignore any subarray having less than five elements).
- Sort each subarray to determine its median. Sorting a small and fixed numbered array takes constant time.
  At the end of this step, we have an array containing medians of all the subarray.
- Recursively call the partitioning algorithm on the array containing medians until we get our pivot.
- Every time the partition procedure needs to find a pivot, it will follow the above three steps.
'''

# solution four
# Best: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Average: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
# Worst: O(nlog(n)) time | O(n) space - where n is the length of the input array
# the worst case time complexity happens when the input array is sorted or if all of its elements are the same
def quickSort(array):
    helper(array, 0, len(array) - 1)
    return array

def helper(arr, low, high):
    if low < high:
        # partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # recursively sort the left part of the array
        helper(arr, low, pivot_index - 1)

        # recursively sort the right part of the array
        helper(arr, pivot_index + 1, high)

def partition(arr, low, high):
    if low == high:
        return low

    # use the median of medians as the pivot, so we find the
    # the median of medians and swap it with the element at index 'high'
    median = medianOfMedians(arr, low, high)
    for i in range(low, high):
        if arr[i] == median:
            arr[i], arr[high] = arr[high], arr[i]
            break

    # choose the last element as the pivot
    pivot = arr[high]
    for i in range(low, high):
        # all elements less than 'pivot' will be before the index 'low'
        if arr[i] < pivot:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1

    # puts the pivot element in its correct sorted position
    arr[low], arr[high] = arr[high], arr[low]

    # return the index of the pivot
    return low

def medianOfMedians(self, arr, low, high):
    # get lenght of the current window on the array that we are working on
    n = high - low + 1

    # if we have less than 5 elements, ignore the partitioning algorithm
    if n < 5:
        # and just return the median, which is at index 'low'
        return arr[low]

    # partition the given array into chunks of 5 elements
    partitions = [arr[j:j + 5] for j in range(low, high + 1, 5)]

    # for simplicity, lets ignore any partition with less than 5 elements
    full_partitions = [partition for partition in partitions if len(partition) == 5]

    # sort all partitions
    sorted_partitions = [sorted(partition) for partition in full_partitions]

    # find median of all partations of length 5,
    # so the median of each partition is at index '2'
    medians = [partition[2] for partition in sorted_partitions]

    return self.partition(medians, 0, len(medians) - 1)