# !difficulty: , !from: https://www.algoexpert.io/questions/heap-sort

'''
Write a function that takes in an array of integers and returns a sorted version of that
array. Use the Heap Sort algorithm to sort the array.

1. Divide the input array into two subarrays in place.
   The second subarray should be sorted at all times and should start with a length of 0,
   while the first subarray should be transformed into a max (or min) heap and should satisfy the heap property at all times.
2. Note that the largest (or smallest) value of the heap should be at the very beginning of the newly-built heap.
   Start by swapping this value with the last value in the heap;
   the largest (or smallest) value in the array should now be in its correct position in the sorted subarray,
   which should now have a length of 1; the heap should now be one element smaller, with its first element out of place.
   Apply the "sift down" method of the heap to re-position this out-of-place value.
3. Repeat the step 2 until the heap is left with only one value, at which point the entire array should be sorted.

Input: [8, 5, 2, 9, 5, 6, 3]
Output: [2, 3, 5, 5, 6, 8, 9]
'''

# Complexity:
# O(nlog(n)) time - best, average, worst,
# because we need to heapify the array first and then we need to sift down n times,
# the heapify costs O(n) time and the sift down costs O(log(n)) time, so the total time complexity is O(nlog(n))
# O(1) space

# solution one iterative from scratch
def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        # Put the first element, which is the highest, at the end of the array
        swap(0, endIdx, array)
        # Heapify the heap again, but ignoring the last element because it is in the position we want
        siftDown(0, endIdx - 1, array)
    return array

def buildMaxHeap(array):
    # The first parent in the heap will always be at this index
    firstParentIdx = (len(array) - 2) // 2
    
    # Start from the first parent and then go backwards to the root, moving to all previous parents
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)

def siftDown(currentIdx, endIdx, heap):
    # Left child will always the at this index due to how heap works
    childOneIdx = currentIdx * 2 + 1

    # While the left child doesn't exceed the heap, so if it exists and is in the heap
    while childOneIdx <= endIdx:
        # Right child will always be at index currentIdx * 2 + 2, if present
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1

        # We need to find the highest between the children,
        # because we want to swap the current with the highest child
        # in case the current is lower than the highest child
        # idxToSwap = childTwoIdx if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx] else childOneIdx
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx

        # If the the current is lower than the highest child, we swap them,
        # otherwise we stop because the heap is heapified
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap)

            # Move the current index where the current will be after the swap,
            # because we want to keep moving it down if needed
            currentIdx = idxToSwap

            # Move the index of the left child to the new left child of the current
            childOneIdx = currentIdx * 2 + 1
        else:
            # the heap is heapified, so we can stop
            return

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# solution two iterative using heapq
# Import the Python STL library “heapq“ to use heap
import heapq

def heapSort(array):
    # Convert the input list into a heap using the “heapify” function from heapq
	heapq.heapify(array)
	result = []
    # Iterate over the heap and extract the minimum element using “heappop” function from heapq
    # and append it to the “result” list, which will be the sorted array at the end
	while array:
		result.append(heapq.heappop(array))
	return result