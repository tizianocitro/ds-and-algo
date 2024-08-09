# Prefix Sum

A **prefix sum** is the cumulative sum of elements in an array up to a certain index. It is a powerful tool for efficiently solving range sum queries and various subarray problems. By precomputing the prefix sums of an array, we can quickly calculate the sum of any subarray in constant time. This technique is widely used in algorithmic problems to improve performance and reduce time complexity, making it essential for handling large datasets and multiple queries efficiently.

For example, if we have an array `[1, 2, 3, 4]`, the prefix sums would be calculated as follows:

- Prefix sum at index `0`: `(1)`
- Prefix sum at index `1`: `(1 + 2 = 3)`
- Prefix sum at index `2`: `(1 + 2 + 3 = 6)`
- Prefix sum at index `3`: `(1 + 2 + 3 + 4 = 10)`

So, the **prefix sum array** for `[1, 2, 3, 4]` is `[1, 3, 6, 10]`.

## Algorithm to Calculate Prefix Sum

1. Initialize an array `prefix` of the same length as the input array `arr`.
2. Set `prefix[0]` to `arr[0]`.
3. For each subsequent element, set `prefix[i]` to `prefix[i - 1] + arr[i]`.
4. Return the `prefix` array.

## Code

```python
class Solution:
    def compute_prefix_sum(self, arr):
        # initialize the prefix array with zeros
        prefix = [0] * len(arr)

        # set the first element of the prefix array
        # to the first element of the input array
        prefix[0] = arr[0]

        # compute the prefix sum for each subsequent element
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] + arr[i]

        # return the computed prefix sum array
        return prefix
```

### Complexity Analysis

- **Time Complexity**: The for-loop runs `n - 1` times, where `n` is the length of the input array, resulting `O(n)` in time.
- **Space Complexity**: The `prefix` array requires `O(n)` space, where `n` is the length of the input array.

## Why Use Prefix Sums?

Prefix sums are used to improve the efficiency of range sum queries. Without a prefix sum, calculating the sum of elements between two indices `i` and `j` in an array requires iterating through the elements from `i` to `j`, which takes `O(n)` time. By precomputing the prefix sums, we can answer these queries in `O(1)` time.

### Example: Range Sum Query

Given an array `nums` and a range query `[i, j]`, find the sum of elements between indices `i` and `j`.

#### Example Input/Output

- Input: arr = [1, 2, 3, 4], i = 1, j = 3
- Output: 9
- Explanation: The sum of 2, 3 and 4 is 9.

#### Step-by-Step Algorithm

1. **Compute the Prefix Sum Array**:
    - Initialize a `prefix` array prefix of the same length as the input array `arr`.
    - Set `prefix[0]` to the first element of the input array.
    - Iterate through the input array starting from index `1`:
        - Set `prefix[i]` to `prefix[i - 1] + arr[i]`.
    - The `prefix` sum array is now ready to be used for range sum queries.
2. **Answer the Range Sum Query**:
    - For a given range `[i, j]`:
        - If `i = 0`, the sum is `prefix[j]`.
        - Otherwise, the sum is `prefix[j] - prefix[i - 1]`.

#### Code

```python
class Solution:
    def compute_prefix_sum(self, arr):
        # initialize the prefix array with zeros
        prefix = [0] * len(arr)

        # set the first element of the prefix array
        # to the first element of the input array
        prefix[0] = arr[0]

        # compute the prefix sum for each subsequent element
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] + arr[i]
        
        # return the computed prefix sum array
        return prefix

    def range_sum_query(self, prefix, i, j):
        # calculate the sum of elements between
        # indices i and j using the prefix array
        if i == 0:
            return prefix[j]
        return prefix[j] - prefix[i - 1]
```

#### Complexity Analysis

Note that `n` is the number of elements in the input array.

- **Time Complexity**:
    - **Computation**: The for-loop runs `n - 1` times, resulting in `O(n)` time.
    - **Range Sum Query**: Answering a range sum query takes `O(1)` time.

- **Space Complexity**:
    - **Prefix Array**: The `prefix` array requires `O(n)` space.

## Applications of Prefix Sums

1. **Range Sum Queries**: As explained above, prefix sums can quickly answer the sum of elements between any two indices in an array.
2. **Subarray Problems**: Prefix sums are used to find subarrays with a given sum, maximum sum subarray, and other subarray-related problems.
3. **2D Prefix Sums**: Extending the concept to two-dimensional arrays helps in efficiently calculating the sum of elements in sub-matrices.
4. **Frequency Counting**: Prefix sums can be used to maintain cumulative frequencies, helping in statistical calculations and data analysis.
5. **Balancing Loads**: In distributed systems, prefix sums can help in balancing workloads evenly across multiple servers.