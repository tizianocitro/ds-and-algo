# !difficulty: medium

# Write a function that takes in a non-empty, unordered array of positive integers and returns the array's majority element
# without sorting the array and without using more than constant space.
# An array's majority element is an element of the array that appears in over half of its indices.
# Note that the most common element of an array (the element that appears the most times in the array) isn't necessarily the array's majority element;
# for example, the arrays [3, 2, 2, 1] and [3, 4, 2, 2, 1] both have 2 as their most common element,
# yet neither of these arrays have a majority element, because neither 2 nor any other element appears in over half of the respective arrays' indices.
# You can assume that the input array will always have a majority element.

# Input: array = [1, 2, 3, 2, 2, 1, 2]
# Output: 2 // 2 appears in 4 out of 7 indices in this array

# solution one which allows the skip of elements
# Complexity:
# O(n) time - where n is the length of the array
# O(1) space
def majorityElement(array):
    currentMajority = None
    counter = 0
    for n in array:
        if counter == 0:
            currentMajority = n
        if currentMajority == n:
            counter += 1
            continue
        counter -= 1        
    return currentMajority

# solution two which does not allow the skip of elements
# Complexity:
# O(n) time - where n is the length of the array
# O(1) space
def majorityElement(array):
    length = len(array)
    currentMajority = array[0]
    counter = 1
    for i in range(1, length):
        current = array[i]
        if currentMajority == current:
            counter += 1
            continue
        counter -= 1
        if counter == 0:
            currentMajority = current
            counter = 1
    return currentMajority

# solution three using sorting
# Complexity:
# O(nlog(n)) time - because of sorting
# O(1) space
def majorityElement(array):
    # if the array is sorted the majority element is in the middle
    # this is better than the brute force solution already
    array.sort()
    majority = len(array) // 2
    return array[majority]

# solution three - brute force
# Complexity:
# O(n^2) time - because of the nested for loop
# O(1) space
def majorityElement(array):
    length = len(array)
    majority = (length // 2) + 1

    for n in array:
        localMajority = majority
        for m in array:
            if m != n:
                continue
            localMajority -= 1
            if localMajority == 0:
                return n

    return -1

# solution with bitwize operations
# Complexity:
# O(n) time - where n is the length of the array
# O(1) space
def majorityElement(array):
    majority = 0

    for currentBit in range(32):
        currentBitValue = 1 << currentBit
        onesCount = 0

        for num in array:
            if (num & currentBitValue) != 0:
                onesCount += 1

        if onesCount > len(array) / 2:
            majority += currentBitValue
    return majority
