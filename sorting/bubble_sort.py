# !difficulty: easy

# Traverse the input array, swapping any two numbers that are out of order and keeping track of any swaps that you make.
# Once you arrive at the end of the array, check if you have made any swaps;
# if not, the array is sorted and you are done;
# otherwise, repeat the steps laid out in this hint until the array is sorted.

# Complexity
# Best: O(n) time | O(1) space - where n is the length of the input array
# Average: O(n^2) time | O(1) space - where n is the length of the input array
# Worst: O(n^2) time | O(1) space - where n is the length of the input array

# solution one
def bubble_sort(array):
    length = len(array) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
    return array

# solution two
# slight optimization on the number of iterations
def bubble_sort(array):
    length = len(array) - 1
    for i in range(length):
        # We can skip the last i numbers
        # because array[length - i] is the greatest number of the previous iteration
        for j in range(length - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array