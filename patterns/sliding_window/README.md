# Sliding Window

In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something among all the subarrays (or sublists) of a given size. For example, consider this problem:

> Given an array, find the average of each subarray of K contiguous elements in it.

Let's understand this problem with an example:

> arr = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5

Here, we are asked to find the average of all subarrays of 5 contiguous elements in the given array. Let's solve this:

1. For the first 5 numbers (subarray from index 0-4), the average is: (1 + 3 + 2 + 6 - 1)/5 = 2.2
2. The average of next 5 numbers (subarray from index 1-5) is: (3 + 2 + 6 - 1 + 4)/5 = 2.8
3. For the next 5 numbers (subarray from index 2-6), the average is: (2 + 6 - 1 + 4 + 1)/5 = 2.4
4. ...

Here is the final output containing the averages of all subarrays of size 5:

> Output: [2.2, 2.8, 2.4, 3.6, 2.8]

A `brute-force algorithm` will calculate the sum of every 5-element subarray of the given array and divide the sum by 5 to find the average. This is what the algorithm will look like:

```python
class Solution:
    def findAverages(self, k, arr):
        result = []
        for i in range(len(arr) - k + 1):
            # find sum of next K elements
            sum = 0.0
            for j in range(i, i + k):
                sum += arr[j]

            # calculate and append average
            result.append(sum / k)

        return result
```

**Time complexity**: Since for every element of the input array, we are calculating the sum of its next K elements, the time complexity of the above algorithm will be `O(n * K)` where N is the number of elements in the input array.

We can find a better solution because there is inefficiency in the solution above.

The inefficiency is that for any two consecutive subarrays of size 5, the overlapping part (which will contain four elements) will be evaluated twice. For example, take the above-mentioned input:

![Inefficiency](/assets/sliding_window_1.png "Visual representation of the inefficiency")

As seen in the image, there are four overlapping elements between the subarray (indexed from 0-4) and the subarray (indexed from 1-5). We have to find a way to somehow reuse the sum we have calculated for the overlapping elements.

The efficient way to solve this problem would be to visualize each subarray as a sliding window of 5 elements. This means that we will slide the window by one element when we move on to the next subarray. To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window. This will save us from going through the whole subarray to find the sum and, as a result, the algorithm complexity will reduce to `O(N)`.

![Visual representation of the algorithm](/assets/sliding_window_2.png "Visual representation of the algorithm")

Here is the algorithm for the Sliding Window approach:

```python
class Solution:
    def findAverages(self, k, arr):
        result = []
        windowSum, windowStart, windowEnd = 0.0, 0, 0

        while windowEnd != len(arr) - 1:
            # add the next element
            windowSum += arr[windowEnd]

            # slide the window, no need to slide if we've not hit the required window size of k
            if windowEnd >= k - 1:
                # calculate and append the average
                result.append(windowSum / k)
                # subtract the element going out
                windowSum -= arr[windowStart]
                # slide the window ahead
                windowStart += 1

            # move the window end to expand the window
            windowEnd += 1

        return result
```

In some problems, the size of the sliding window is not fixed. We have to expand or shrink the window based on the problem constraints.