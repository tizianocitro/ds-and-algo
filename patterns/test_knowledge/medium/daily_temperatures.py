# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/daily-temperatures-medium

'''Problem:
You are given a list of daily temperatures. Your task is to return an answer array such that answer[i] is
the number of days you would have to wait until a warmer temperature for each of the days.
If there is no future day for which this is possible, put 0 instead.

Input: [45, 50, 40, 60, 55]
Output: [1, 2, 1, 0, 0]
Explanation: The next day after the first day is warmer (50 > 45). Two days after the second day, the temperature is warmer (60 > 50).
The next day after the third day is warmer (60 > 40). There are no warmer days after the fourth and fifth days.

Input: [80, 75, 85, 90, 60]
Output: [2, 1, 1, 0, 0]
Explanation: Two days after the first day, the temperature is warmer (85 > 80). The next day after the second day is warmer (85 > 75).
The next day after the third day is warmer (90 > 85). There are no warmer days after the fourth and fifth days.

Input: [32, 32, 32, 32, 32]
Output: [0, 0, 0, 0, 0]
Explanation: All the temperatures are the same, so there are no warmer days ahead.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input list
# O(n) space - because we are using a stack to store the indices of the input list
class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)

        stack = []
        for i, temp in enumerate(temperatures):
            # while the stack is not empty and the current temperature is higher
            # than the temperature at the index stored at the top of the stack
            while stack and stack[-1][0] < temp:
                _, j = stack.pop()
                # calculate the number of days until warmer temperature,
                # by subtracting the current index from the index stored at the top of the stack
                res[j] = i - j
            stack.append((temp, i))

        return res

# solution two is slightly different than solution one
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