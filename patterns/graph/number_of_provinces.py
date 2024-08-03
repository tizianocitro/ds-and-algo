# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/651a8380aa7cf9c7c20f9aa8

'''Problem:
Imagine a country with several cities. Some cities have direct roads connecting them, while others might be connected through a sequence of intermediary cities.
Using a matrix representation, if matrix[i][j] holds the value 1, it indicates that city i is directly linked to city j and vice versa.
If it holds 0, then there's no direct link between them.

Determine the number of separate city clusters (or provinces).

A province is defined as a collection of cities that can be reached from each other either directly or through other cities in the same province.

Input: [[1,1,0], [1,1,0], [0,0,1]]
Output: 2
Explaination: there are two provinces: cities 0 and 1 form one province, and city 2 forms its own province.

Input: [[1,0,0,1], [0,1,1,0], [0,1,1,0], [1,0,0,1]]
Output: 2
Explaination: there are two provinces: cities 0 and 3 are interconnected forming one province, and cities 1 and 2 form another.
'''

'''Other solutions:
Look at the patterns/union_find/number_of_provinces.py file for other solutions to this problem.
'''

# solution one recursive
# Complexity:
# O(v^2) time - where v is the number of cities
# the dfs has a for loop that runs through all the neighbors of the current node,
# thus combined with the for that runs for each node in the graph in the findCircleNum,
# the time complexity is O(n^2), and this is especially true when the graph is not connected
# and the we have to run dfs on all the nodes because the check ''if node not in visited'' always returns True.
# O(v) space - where n is the number of cities
class Solution:
    def findCircleNum(self, is_connected) -> int:
        provinces = 0
        number_of_nodes = len(is_connected)
        visited = set()
        # this will be run for each node in the graph that has not been visited,
        # if the graph is not connected, this will be run for all the nodes
        for node in range(number_of_nodes):
            if node not in visited:
                self.dfs(is_connected, node, visited)
                provinces += 1
        return provinces

    def dfs(self, graph, start, visited):
        visited.add(start)
        number_of_nodes = len(graph)
        # this for runs through all the neighbors of the current node,
        # thus combined with the for that runs for each node in the graph,
        # the time complexity is O(n^2) because we must always check all nodes in the array
        # indicating if there is a connection between the current node and the neighbor
        for neighbor in range(number_of_nodes):
            if neighbor not in visited and graph[start][neighbor] == 1:
                self.dfs(graph, neighbor, visited)

# solution two iterative
# Complexity:
# O(v^2) time - where v is the number of cities
# the dfs has a for loop that runs through all the neighbors of the current node,
# thus combined with the for that runs for each node in the graph,
# the time complexity is O(n^2), and this is especially true when the graph is not connected
# and the we have to run dfs on all the nodes because the check ''if node in visited'' always returns False.
# O(v) space - where n is the number of cities
class Solution:
    def findCircleNum(self, is_connected) -> int:
        return self.dfs(is_connected)

    def dfs(self, graph):
        provinces = 0
        number_of_nodes = len(graph)
        visited = set()
        # this will be run for each node in the graph that has not been visited,
        # if the graph is not connected, this will be run for all the nodes
        for node in range(number_of_nodes):
            if node in visited:
                continue

            stack = [node]
            while stack:
                curr = stack.pop()
                visited.add(curr)
                # this for runs through all the neighbors of the current node,
                # thus combined with the for that runs for each node in the graph,
                # the time complexity is O(n^2) because we must always check all nodes in the array
                # indicating if there is a connection between the current node and the neighbor
                for neighbor in range(number_of_nodes):
                    if neighbor not in visited and graph[curr][neighbor] == 1:
                        stack.append(neighbor)
            provinces += 1

        return provinces

# solution three iterative
# Complexity:
# O(v^2) time - where v is the number of cities
# the dfs has a for loop that runs through all the neighbors of the current node,
# thus combined with the for that runs for each node in the graph,
# the time complexity is O(n^2), and this is especially true when the graph is not connected
# and the we have to run dfs on all the nodes because the check ''if node in visited'' always returns False.
# O(v^2) space - where n is the number of cities, because of the graph
# in the worst case, each node can have connections to every other node, resulting in O(v^2) space complexity for the adjacency list.
class Solution:
    def findCircleNum(self, is_connected) -> int:
        number_of_nodes = len(is_connected)
        graph = {i: [] for i in range(number_of_nodes)}
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                if i != j and is_connected[i][j] == 1:
                    graph[i].append(j)

        return self.dfs(graph)

    def dfs(self, graph):
        provinces = 0
        visited = set()
        # this will be run for each node in the graph that has not been visited,
        # if the graph is not connected, this will be run for all the nodes
        for node in range(len(graph)):
            if node in visited:
                continue

            stack = [node]
            while stack:
                curr = stack.pop()
                visited.add(curr)
                # this for runs through all the neighbors of the current node,
                # thus combined with the for that runs for each node in the graph,
                # the time complexity is O(n^2) because we must always check all nodes in the array
                # indicating if there is a connection between the current node and the neighbor
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            provinces += 1

        return provinces
