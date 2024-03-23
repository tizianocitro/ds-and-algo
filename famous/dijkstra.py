# !difficulty: hard, !from: https://www.algoexpert.io/questions/dijkstra's-algorithm

'''Problem:
You're given an integer start and a list edges of pairs of integers. The list is an adjacency list, and it represents a graph.
The number of vertices in the graph is equal to the length of edges, where each index i in edges contains vertex i's outbound edges, in no particular order.
Each individual edge is represented by a pair of two numbers, [destination, distance], where the destination is a positive integer denoting the
destination vertex and the distance is a positive integer representing the length of the edge (the distance from vertex i to vertex destination).
Note that these edges are directed, meaning that you can only travel from a particular vertex to its destination,
not the other way around (unless the destination vertex itself has an outbound edge to the original vertex).
Write a function that computes the lengths of the shortest paths between start and all of the other vertices in the graph using Dijkstra's algorithm and returns them in an array.
Each index i in the output array should represent the length of the shortest path between start and vertex i.
If no path is found from start to vertex i, then output[i] should be -1.

Note that the graph represented by edges won't contain any self-loops (vertices that have an outbound edge to themselves) and will only have positively weighted edges (i.e., no negative distances).

Input:
    start = 0,
    edges = [
        [[1, 7]],
        [[2, 6], [3, 20], [4, 3]],
        [[3, 14]],
        [[4, 2]],
        [],
        [],
    ]
Output: [0, 7, 13, 27, 10, -1]
'''

# solution one with array
# Complexity:
# O(v^2 + e) time - where v is the number of vertices and e is the number of edges
# O(v) because we visit all nodes and for each node we need O(v) to find the node with min distance
# O(e) because for each node, we vist all of each edges, so across all nodes we visit all edges
# (v) spaces - where v is the number of vertices, because we store all nodes in the visited if all nodes are reacheable
# and because we store the min distance for each node
def dijkstrasAlgorithm(start, edges):
    # edges is an ajacency list, meaning that its length is the same as the number of nodes
    numberOfNodes = len(edges)

    # init min distances to all nodes to be inf
    minDistances = [float('inf') for _ in range(numberOfNodes)]

    # set the distance of the start node to 0, in this way,
    # the first node to be selected by the getNodeWithMinDistance will be the start node
    minDistances[start] = 0

    # keep track of visited nodes  
    visited = set()

    # iterate until we visit all the nodes
    while len(visited) != numberOfNodes:
        # get the node with the min distance, which will be the start node at the beginning
        currentNode, currentMinDistance = getNodeWithMinDistance(minDistances, visited)

        # if the current node with min distance has a distance of inf,
        # it means there is no path to it from other nodes, meaning it's not reacheable
        # all other nodes available are with distance inf because the min distance was now inf,
        # so no need to consider them, we can break
        if currentMinDistance == float('inf'):
            break

        # add the node to visited nodes
        visited.add(currentNode)

        # visit all node's outgoing edges to updated their target node distances,
        # if we find better a better way to reach them
        for edge in edges[currentNode]:
            targetNode, distanceToTarget = edge

            # if the target node has already been visited, it means it has a smaller distance
            # compared to the current one, meaning every new distance cannot be shorter
            # than the one already set for it, so we can skip it
            if targetNode in visited:
                continue

            # upddate the distance if already exists by adding the distance of the current node
            # to the distance of the target node and checking if the distance
            # currently set for it in the minDistances is bigger, if it is, then we update it
            newDistanceToTarget = currentMinDistance + distanceToTarget
            oldDistanceToTarget = minDistances[targetNode]
            if newDistanceToTarget < oldDistanceToTarget:
                minDistances[targetNode] = newDistanceToTarget

    # return the min distances by changing inf with -1
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances))

def getNodeWithMinDistance(distances, visited):
    minDistance = float('inf')
    minNode = None

    for node, distance in enumerate(distances):
        # if a node has already been visited we do not want to visit it again
        if node in visited:
            continue

        if distance <= minDistance:
            minDistance = distance
            minNode = node

    return minNode, minDistance

# solution two with heap
# Complexity:
# O((v + e)lognv) time - where v is the number of vertices and e is the number of edges
# O(v) because we visit all nodes and for each node we need O(logv) to get the node with min distance and ensure the heap remains heapified
# O(e) because for each node, we vist all of each edges, so across all nodes we visit all edges
# but for each edge we also need to update its value if the new distance is smaller,
# and updating the value means updating the heap to ensure it remains heapified, which takes O(logv)
# (v) spaces - where v is the number of vertices, because we store all nodes in the heap and because we store the min distance for each node
def dijkstrasAlgorithm(start, edges):
    # edges is an ajacency list, meaning that its length is the same as the number of nodes
    numberOfNodes = len(edges)

    # init min distances to all nodes to be inf and set the distance of the start node to 0 as needed
    minDistances = [float('inf') for _ in range(numberOfNodes)]
    minDistances[start] = 0

    # init the heap and ensure the start node is the top of the heap
    # we will use the heap to get the node with min distance
    # it also substitutes the visisted set because when empty it indicates we have visited all nnodes
    minDistancesHeap = MinHeap([(n, float('inf')) for n in range(numberOfNodes)])
    minDistancesHeap.update(start, 0)

    # iterate until we visit all the nodes
    while not minDistancesHeap.isEmpty():
        # get the node with the min distance, which will be the start node at the beginning
        currentNode, currentMinDistance = minDistancesHeap.remove()

        # if the current node with min distance has a distance of inf,
        # it means there is no path to it from other nodes, meaning it's not reacheable
        # all other nodes available are with distance inf because the min distance was now inf,
        # so no need to consider them, we can break
        if currentMinDistance == float('inf'):
            break

        # visit all node's outgoing edges to updated their target node distances,
        # if we find better a better way to reach them
        for edge in edges[currentNode]:
            targetNode, distanceToTarget = edge

            # upddate the distance if already exists by adding the distance of the current node
            # to the distance of the target node and checking if the distance
            # currently set for it in the minDistances is bigger, if it is, then we update it
            newDistanceToTarget = currentMinDistance + distanceToTarget
            oldDistanceToTarget = minDistances[targetNode]
            if newDistanceToTarget < oldDistanceToTarget:
                minDistances[targetNode] = newDistanceToTarget
                minDistancesHeap.update(targetNode, newDistanceToTarget)

    # return the min distances by changing inf with -1
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances))

# min heap class used in the second solution
class MinHeap:
    def __init__(self, array):
        # Holds the position in the heap that each vertex is at
        self.vertexMap = {idx: idx for idx in range(len(array))}
        self.heap = self.buildHeap(array)
    
    def isEmpty(self):
        return len(self.heap) == 0

    # 0(n) time | 0(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # 0(log(n)) time | 0(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1 
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap][1] < heap[currentIdx][1]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    # 0(log(n)) time | 0(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # 0(log(n)) time | 0(1) space
    def remove(self):
        if self.isEmpty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()
        self.vertexMap.pop(vertex)
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return vertex, distance

    def swap(self, i, j, heap):
        self.vertexMap[heap[i][0]] = j
        self.vertexMap[heap[j][0]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def update(self, vertex, value):
        self.heap[self.vertexMap[vertex]] = (vertex, value)
        self.siftUp(self.vertexMap[vertex], self.heap)