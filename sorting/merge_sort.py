# Merge Sort works by cutting an array in two halves, respectively sorting those two halves by performing some special logic,
# and then merging the two newly-sorted halves into one sorted array.
# The respective sorting of the two halves is done by reapplying the Merge Sort algorithm / logic on each half until single-element halves are obtained;
# these single-element arrays are sorted by nature and can very easily be merged back together.

# Divide the input array in two halves by finding the middle-most index in the array and slicing the two halves around that index.
# Then, recursively apply Merge Sort to each half, and finally merge them into one single,
# sorted array by iterating through their values and progressively adding them to the new array in ascending order.

# Your implementation of Merge Sort almost certainly uses a lot of auxiliary space and likely does not sort the input array in place.
# What is the space complexity of your algorithm? Can you implement a version of the algorithm using only one additional array of the same length as the input array,
# and can this version sort the input array in place?

# Complexity
# Best: O(nlog(n)) time | O(n) space - where n is the length of the input array
# Average: O(nlog(n) time | O(n) space - where n is the length of the input array
# Worst: O(nlog(n)) time | O(n) space - where n is the length of the input array 
# Memory is n instead of nlog(n) because we create a single array at the start, which is a copy of the original array,
# so we can ignore the log(n) coming from recursion. In fact, it would be O(n + log(n))

# solution one
def merge_sort(main_array):
    # clone_array = [n for n in array]
    clone_array = main_array[:]
    helper(main_array, clone_array, 0, len(main_array))
    return clone_array

def helper(main_array, clone_array, start_idx, end_idx):
    if end_idx - start_idx <= 1:
        return

    middle_idx = (end_idx + start_idx) // 2
    helper(clone_array, main_array, start_idx, middle_idx)
    helper(clone_array, main_array, middle_idx, end_idx)

    i = start_idx
    j = middle_idx
    k = start_idx
    while i < middle_idx and j < end_idx:
        if main_array[i] < main_array[j]:
            clone_array[k] = main_array[i]
            i += 1
        else:
            clone_array[k] = main_array[j]
            j += 1
        k += 1

    while i < middle_idx:
        clone_array[k] = main_array[i]
        i += 1
        k += 1

    while j < end_idx:
        clone_array[k] = main_array[j]
        j += 1
        k += 1

# Complexity
# Best: O(nlog(n)) time | O(nlog(n)) space - where n is the length of the input array
# Average: O(nlog(n) time | O(nlog(n)) space - where n is the length of the input array
# Worst: O(nlog(n)) time | O(nlog(n)) space - where n is the length of the input array (due to bad pivot choice)

# solution two
def merge_sort(array):
    if len(array) <= 1:
        return array

    left_array = array[:len(array) // 2]
    right_array = array[len(array) // 2:]

    merge_sort(left_array)
    merge_sort(right_array)

    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

    return array