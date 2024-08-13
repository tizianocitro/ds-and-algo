# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/64c151c7505e25aa946412b6

'''Problem:
Given an array of integers temperatures representing daily temperatures,
your task is to calculate how many days you have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

Input: temperatures = [70, 73, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation: The first day's temperature is 70 and the next day's temperature is 73 which is warmer.
So for the first day, you only have to wait for 1 day to get a warmer temperature.
Hence, the first element in the result array is 1. The same process is followed for the rest of the days.
'''

'''Solution:
We will use a stack to store the indices of the temperatures array.
We iterate over the array, and for each temperature, we check whether the current temperature is greater than the temperature at the index on the top of the stack.
If it is, we update the corresponding position in the result array and pop the index from the stack.

1. Initialize an empty stack to store the indices of the temperatures array.
   Also, initialize a result array of the same length as temperatures with all values set to 0.

2. Iterate over the temperatures array. For each temperature:
    1. While the stack is not empty and the current temperature is greater than the temperature at the index on the top of the stack,
       set the value in the result array at the top index of the stack to the difference between the current index and the top index of the stack.
       Pop the index from the stack.
    2. Push the current index onto the stack.

3. Return the result array.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input list
# O(n) space - because we are using a stack to store the indices of the input list
class Solution:
    def dailyTemperatures(self, temperatures):
        # initialize empty stack and a result list with zeros
        stack, res = [], [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            # while the stack is not empty and the current temperature is higher
            # than the temperature at the index stored at the top of the stack
            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                # calculate the number of days until warmer temperature,
                # by subtracting the current index from the index stored at the top of the stack
                res[top] = i - top
            stack.append(i)
        return res