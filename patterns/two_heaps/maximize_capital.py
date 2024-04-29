# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639c960d0ce4573267ea5666

'''Problem:
Given a set of investment projects with their respective profits, we need to find the most profitable projects.
We are given an initial capital and are allowed to invest only in a fixed number of projects.
Our goal is to choose projects that give us the maximum profit.
Write a function that returns the maximum total capital after selecting the most profitable projects.

We can start an investment project only when we have the required capital.
After selecting a project, we can assume that its profit has become our capital, and that we have also received our capital back.

Input: Project Capitals = [0, 1, 2], Project Profits = [1, 2, 3], Initial Capital = 1, Number of Projects = 2
Output: 6
Explanation:
    1. With initial capital of 1, we will start the second project which will give us profit of 2.
       Once we selected our first project, our total capital will become 3 (profit + initial capital).
    2. With 3 capital, we will select the third project, which will give us 3 profit.
    3. After the completion of the two projects, our total capital will be 6 (1+2+3).

Input: Project Capitals = [0, 1, 2, 3], Project Profits = [1, 2, 3, 5], Initial Capital = 0, Number of Projects = 3
Output: 8
Explanation:
    1. With 0 capital, we can only select the first project, bringing out capital to 1.
    2. Next, we will select the second project, which will bring our capital to 3.
    3. Next, we will select the fourth project, giving us a profit of 5.
    4. After selecting the three projects, our total capital will be 8 (1+2+5).
'''

# solution one with heaps keeping track of the lowest capital projects
# with indexes to map the capital to the corresponding profit
# Complexity:
# O(nlogn + klogn) where k is the number of projects and n is the number of profits/capitals
# O(n) for creating the two heaps for capitals and profits
from heapq import *

class Solution:
    def findMaximumCapital(self, capitals, profits, numberOfProjects, initialCapital):
        # O(n) for heapify -> https://github.com/python/cpython/blob/v3.10.7/Lib/heapq.py
        min_capitals_heap = [(capital, i) for i, capital in enumerate(capitals)]
        heapify(min_capitals_heap)
        max_profits_heap = []
        heapify(max_profits_heap)

        capital = initialCapital

        # O(nlogn + klogn) where k is the number of projects and n is the number of profits/capitals
        # this is because each capital/profit is pushed to the heap once and popped once,
        # for example, if all capitals are less than the initial capital, we will have to pop all the capitals
        # and push all the profits to the heap, but starting from the second iteration, we will only have to pop from the max heap
        # until we have the required number of projects or no more projects are available
        for _ in range(numberOfProjects):
            # find all projects that can be selected within the available capital
            # and insert the related profits in the max-heap
            while min_capitals_heap and min_capitals_heap[0][0] <= capital:
                min_capital = heappop(min_capitals_heap)
                heappush(max_profits_heap, -profits[min_capital[1]])
            
            # if we have projects left but we are not able to find any project
            # that can be completed within the available capital, we terminate
            if not max_profits_heap:
                break

            # select the project with the maximum profit
            capital += -heappop(max_profits_heap)

        return capital

# solution two with heaps keeping track of the highest profitable projects
# with indexes to map the profit to the corresponding capital
# Complexity:
# O(knlogn) where n is the number of profits and k is the number of projects
# O(n) for creating the main and sub heaps
from heapq import *

class Solution:
    def findMaximumCapital(self, capitals, profits, numberOfProjects, initialCapital):
        # O(n) where n is the number of profits -> https://github.com/python/cpython/blob/v3.10.7/Lib/heapq.py
        main_profits_heap = [(-profit, i) for i, profit in enumerate(profits)]
        sub_profits_heap = []
        heapify(main_profits_heap)
        heapify(sub_profits_heap)

        capital = initialCapital

        # O(knlogn) where k is the number of projects and n is the number of profits/capitalx
        for _ in range(numberOfProjects):
            if not sub_profits_heap or (main_profits_heap and -main_profits_heap[0][0] >= -sub_profits_heap[0][0]):
                # in the worst case, we will have to pop all the profits from the main heap each time this function is called
                capital += self.get_most_profitable_project(main_profits_heap, sub_profits_heap, capitals, capital)
            else:
                # in the worst case, we will have to pop all the profits from the sub heap each time this function is called
                capital += self.get_most_profitable_project(sub_profits_heap, main_profits_heap, capitals, capital)

        return capital

    # O(nlogn) where n is the number of profits, because in the worst case we will have to pop all the profits
    # which takes O(n) time but each pop operation takes O(logn) time
    # in the worst case, we will have to pop all the profits from the main heap each time this function is called
    def get_most_profitable_project(self, main_profits_heap, sub_profits_heap, capitals, capital):
        highest_profit = heappop(main_profits_heap)
        while capitals[highest_profit[1]] > capital:
            if not main_profits_heap:
                return 0

            heappush(sub_profits_heap, highest_profit)
            highest_profit = heappop(main_profits_heap)

        return -highest_profit[0]