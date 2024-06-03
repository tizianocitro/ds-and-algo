# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a37843a41249d4abecb89a

'''Problem:
Given an N * N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
], 
K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
'''

# solution one is the same as solution two with k-way merge but uses an optimization
# Complexity:
# O(n + klogn) time - where n is the number of rows in the matrix and k is the input k
# O(n) space - where n is the number of rows in the matrix
from heapq import *

class Solution:
    def findKthSmallest(self, matrix, k):
        min_heap = []

        # put the 1st element of each row in the min heap
        # we don't need to push more than 'k' elements in the heap
        for i in range(min(k, len(matrix))):
            heappush(min_heap, (matrix[i][0], i, 1))

        kth_min_num = 0
        for i in range(k):
            ith_min_num, list_ix, next_num_ix = heappop(min_heap)

            if next_num_ix < len(matrix[list_ix]):
                heappush(min_heap, (matrix[list_ix][next_num_ix], list_ix, next_num_ix + 1))

            kth_min_num = ith_min_num

        return kth_min_num

# solution two using k-way merge
# Complexity:
# O(n + klogn) time - where n is the number of rows in the matrix and k is the input k
# O(n) space - where n is the number of rows in the matrix
from heapq import *

class Solution:
    def findKthSmallest(self, matrix, k):
        min_heap = []

        for i in range(len(matrix)):
            if len(matrix[i]) > 0:
                heappush(min_heap, (matrix[i][0], i, 1))

        kth_min_num = 0
        for i in range(k):
            ith_min_num, list_ix, next_num_ix = heappop(min_heap)

            if next_num_ix < len(matrix[list_ix]):
                heappush(min_heap, (matrix[list_ix][next_num_ix], list_ix, next_num_ix + 1))

            kth_min_num = ith_min_num

        return kth_min_num

'''Bynary Search Solution:
The biggest problem to use Binary Search, in this case, is that we don’t have a straightforward sorted array,
instead, we have a matrix. In Binary Search, we calculate the middle index of the search space (1 to N)
and see if our required number is pointed out by the middle index; if not we either search in the lower half or the upper half.
In a sorted matrix, we can’t really find a middle. Even if we do consider some index as middle,
it is not straightforward to find the search space containing numbers bigger or smaller than the number pointed out by the middle index.

An alternative could be to apply the Binary Search on the “number range” instead of the “index range”.
The smallest number of the matrix is at the top left corner and the biggest number is at the bottom right corner.
These two numbers can represent the “range” i.e., the start and the end for the Binary Search.

The algorithm will work as follows:
1. Start the Binary Search with start = matrix[0][0] and end = matrix[n-1][n-1].
2. Find middle of the start and the end. This middle number is NOT necessarily an element in the matrix.
3. Count all the numbers smaller than or equal to middle in the matrix. As the matrix is sorted, we can do this in O(N).
4. While counting, we can keep track of the “smallest number greater than the middle” (let’s call it n1) and at the same time
   the “biggest number less than or equal to the middle” (let’s call it n2). These two numbers will be used to adjust
   the “number range” for the Binary Search in the next iteration.
5. If the count is equal to K, n2 will be our required number as it is the “biggest number less than or equal to the middle”, and is definitely present in the matrix.
6. If the count is less than K, we can update start = n2 to search in the higher part of the matrix and if the count is greater than K,
   we can update end = n1 to search in the lower part of the matrix in the next iteration.

Here is the visual representation of the algorithm using markdown:

![Visual representation of the algorithm](/assets/k-way_merge/binary_search_in_matrix.png "Visual representation of the algorithm")
'''

# solution three using binary search
# Complexity:
# O(nlog(max-min)) time - where n is the number of rows in the matrix
# and max and min are the smallest and largest elements in the matrix
# The binary search could take log(max−min) iterations where ‘max’ is the largest
# and ‘min’ is the smallest element in the matrix and in each iteration we take O(n)
# for counting, therefore, the overall time complexity will be O(nlog(max-min)).
# O(1) space
class Solution:
    def findKthSmallest(self, matrix, k):
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

            count, smaller, larger = self.count_less_equal(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k: # search higher
                start = larger
            else: # search lower
                end = smaller

        return start

    def count_less_equal(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)

        # start at the first column of the last row
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                # as matrix[row][col] is bigger than the mid, let's keep track
                # of the smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                # as matrix[row][col] is less than or equal to the mid, let's keep track
                # of the biggest number less than or equal to the mid
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger
