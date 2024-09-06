# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/all-tasks-scheduling-orders-hard

'''Problem:
There are N tasks, labeled from 0 to N-1. Each task can have some prerequisite tasks
which need to be completed before it can be scheduled.

Given the number of tasks and a list of prerequisite pairs, write a method to
print all possible ordering of tasks meeting all prerequisites.

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output: 
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: 
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
'''

'''
At any stage, if we have more than one source available and since we can choose any source,
therefore, in this case, we will have multiple orderings of the tasks.
We can use a recursive approach with Backtracking to consider all sources at any step.

1. Initialize and build the Graph.
2. Find All Source.
3. Print All Topological Sorts:
    - Use a recursive function to explore all possible topological sorts.
    - For each source:
        - Add the source to the sortedOrder list.
        - Remove the source from the queue.
        - Decrement the in-degrees of its children.
        - If a child's in-degree becomes 0, add it to the queue.
        - Recursively call the function with the updated queue and sorted order.
        - Backtrack by removing the source from the sorted order and restoring the in-degrees of its children.
4. Check for Cycles: if the sortedOrder list contains all tasks, add it to the orders list.
'''

# solution one
# Complexity:
# O(v! * e) time - where v is the number of tasks and e is the number of prerequisites
# the e term is needed because in each recursive call, at max, we remove (and add back) all the edges.
# O(v! * e) space - since we have to store all of the topological sorts
from collections import deque

class Solution:
    def __init__(self):
        self.orders = []

    def printOrders(self, tasks, prerequisites):
        sorted_order = []
        if tasks < 1:
            return self.orders

        # count of incoming edges
        in_degrees = {i: 0 for i in range(tasks)}
        # adjacency list graph
        graph = {i: [] for i in range(tasks)}

        # build the graph
        for parent, child in prerequisites:
            # put the child into it's parent's list
            graph[parent].append(child)
            # increment child's in-degree
            in_degrees[child] += 1

        # find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for node in in_degrees:
            if in_degrees[node] == 0:
                sources.append(node)

        # recursive function to print all topological sorts of the graph, backtracking
        self.printAllTopologicalSorts(graph, in_degrees, sources, sorted_order)

        return self.orders

    def printAllTopologicalSorts(self, graph, in_degrees, sources, sorted_order):
        # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency between 
        # tasks, or we have not processed all the tasks in this recursive call
        if len(sorted_order) == len(in_degrees):
            self.orders.append(sorted_order.copy())

        if sources:
            for source in sources:
                sorted_order.append(source)

                # make a copy of sources
                next_sources = deque(sources)

                # only remove the current source, all other sources should
                # remain in the queue for the next call
                next_sources.remove(source)

                # get the node's children to decrement their in-degrees
                for child in graph[source]:
                    in_degrees[child] -= 1
                    if in_degrees[child] == 0:
                        next_sources.append(child)

                    # recursive call to print other orderings from the remaining (and new) sources
                    self.printAllTopologicalSorts(graph, in_degrees, next_sources, sorted_order)

                    # backtrack, remove the source from the sorted order and put all of its children 
                    # back to consider the next source instead of the current source
                    sorted_order.remove(source)
                    for child in graph[source]:
                        in_degrees[child] += 1

        # here is equivalent to the same if statement at the beginning
        # of the function, you can do it here or there
        # if len(sorted_order) == len(in_degrees):
        #     self.orders.append(sorted_order.copy())
