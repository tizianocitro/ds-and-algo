# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/problem-challenge-2-minimum-height-trees-hard

'''Problem:
We are given an undirected graph that has the characteristics of a k-ary tree.
In such a graph, we can choose any node as the root to make a k-ary tree.
The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT).
There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs.
Write a method to find all MHTs of the given graph and return a list of their roots.

Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
Output:[1, 2]
Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the height of the trees with roots '1' or '2' is three which is the minimum.

Input: vertices: 4, Edges: [[0, 1], [0, 2], [2, 3]]
Output:[0, 2]
Explanation: Choosing '0' or '2' as roots give us MHTs. In the below diagram, we can see that the height of the trees with roots '0' or '2' is three which is minimum.

Input: vertices: 4, Edges: [[0, 1], [1, 2], [1, 3]]
Output:[1]
'''

# solution one using bfs and backtracking
# Complexity:
# O(v(v + e)) time - where v is the number of nodes and e is the number of edges
# O(v + e) space - where v is the number of nodes and e is the number of edges
from heapq import *
from collections import deque

class Solution:
    def findTrees(self, nodes, edges):
        # if there is no node, return empty list
        if nodes < 1:
            return []

        # build graph and in_degrees
        in_degrees, graph = self.buildGraph(nodes, edges)

        # build a max heap to iterate through the nodes by their in-degrees
        # from the node with the highest in-degree to the lowest
        # this takes O(vlogv) time and O(v) space because we are iterating
        # through all the nodes and adding them to the max heap (O(logv) time)
        max_heap = []
        for node in range(nodes):
            heappush(max_heap, (-in_degrees[node], node))

        # bfs to find the mht roots
        return self.bfs(graph, max_heap)

    # bfs to find the minimum height trees roots
    # in the worst case, we iterate the while loop for all the nodes in the
    # max heap because they all produce a tree with the same height
    # each iteration takes O(logv) for the heappop and O(v + e) for the bfs
    # while using O(v) space for the queue and visited set, so
    # the total time complexity is O(v(v + e)) and the space complexity is O(v)
    def bfs(self, graph, max_heap):
        min_height = float('inf')
        roots = []

        # iterate through the nodes by their in-degrees
        # until there are no more nodes in the max heap
        # or the height of the current tree is greater than the minimum height
        while max_heap:
            # pop the node with the highest in-degree, i.e. the root of the tree
            _, root = heappop(max_heap)

            # queue and visited set for bfs, add the root to both
            q, visited = deque(), set()
            q.append(root)
            visited.add(root)

            # start with height 0 and increment it by 1 for each level
            height = 0
            while q:
                level_size = len(q)
                for _ in range(level_size):
                    node = q.popleft()
                    visited.add(node)
                    for child in graph[node]:
                        if child not in visited:
                            q.append(child)
                height += 1

            # if the height of the current tree is less than the minimum height
            # update the minimum height and the roots list
            if height < min_height:
                min_height = height
                roots = [root]
            # if the height of the current tree is equal to the minimum height
            # just add the root to the roots list because it is a new mht root
            elif height == min_height:
                roots.append(root)
            else: # if the height of the current tree is greater than the minimum height, break
                break

        return roots

    # this takes O(v + e) time and O(v + e) space,
    # where v is the number of nodes and e is the number of edges
    def buildGraph(self, nodes, edges):
        in_degrees = {node: 0 for node in range(nodes)}
        graph = {node: [] for node in range(nodes)}
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
            in_degrees[parent] += 1
            in_degrees[child] += 1

        return in_degrees, graph

'''Solution using the Leaf Pruining algorithm:
The key intuition behind solving this problem is based on the definition of a tree's height:
the height of a tree is the number of edges on the longest path between the root and any leaf.
So, an MHT is a tree that minimizes this longest path.

Imagine we have a longest path P in the tree. The path P has two ends; let's call them end A and end B.
Now, let's consider what the root of an MHT can be:

    - If we select a root that is not on the path P, the height of the tree would at least be the length of P,
      because there would be a path from the root to either A or B that is longer than P (as it includes P plus some additional edges).
      Therefore, the root of the MHT must be on P.
    - If the root is on P, but not in the middle of P, then the height of the tree will be larger than if we selected the root in the middle of P,
      because the longest path will be from the root to either end of P. Therefore, the root of the MHT must be in the middle of P.

So, the problem of finding the MHT root(s) reduces to finding the middle node(s) of the longest path in the tree.

We can find the middle node(s) of the longest path by using an algorithm called 'Leaf Pruining'. Let's look into this.

From the above discussion, we can deduce that the leaves can’t give us MHT, hence, we can remove them from the graph and remove their edges too.
Once we remove the leaves, we will have new leaves. Since these new leaves can’t give us MHT, we will repeat the process and remove them from the graph too.
We will prune the leaves until we are left with one or two nodes which will be our answer and the roots for MHTs.

The algorithm works because when you trim leaves, you're essentially trimming the ends of all the longest paths in the tree.
If there's one longest path, you're trimming it from both ends, and if there are multiple longest paths, you're trimming them all.
Eventually, you're left with one or two nodes, which must be the middle of the longest path(s), and those are the roots of the MHTs.

We can implement the above process using the topological sort. Any node with only one edge (i.e., a leaf) can be our source and,
in a stepwise fashion, we can remove all sources from the graph to find new sources.
We will repeat this process until we are left with one or two nodes in the graph, which will be our answer.

This algorithm is used to find the root nodes of the Minimum Height Trees (MHTs) in a graph.
An MHT is a tree rooted at a specific node that minimizes the tree's height.
In a graph with 'n' nodes, there can be one or two MHTs.

Here's a breakdown of the algorithm:

    1. It starts by checking if the number of nodes is less than or equal to 0, returning an empty list if true,
       as there would be no trees in the graph. If the graph contains only one node, it returns that single node as an MHT.
    2. Next, it initializes two HashMaps, in_degrees to store the count of incoming edges for every vertex and
       graph as an adjacency list representation of the graph. It populates these HashMaps with initial values.
    3. The algorithm then constructs the graph. As it's an undirected graph, each edge connects two nodes bi-directionally,
       meaning it adds a link for both nodes and increments the in-degrees of the two nodes.
    4. The algorithm finds all leaf nodes (nodes with only one in-degree) and adds them to a queue.
    5. Next, it iteratively removes the leaf nodes level by level, subtracting one from the in-degree of each leaf node's children.
       If a child node becomes a leaf node as a result, it is added to the queue of leaf nodes. This process repeats until the graph
       has been reduced to one or two nodes, which represent the roots of the MHTs.
    6. Finally, the algorithm adds the remaining nodes in the leaves queue to minHeightTrees and returns this list.
       These nodes are the roots of the MHTs in the graph.
'''

# solution two using the leaf pruning algorithm implemented with topological sort
# Complexity:
# O(v + e) time - where v is the number of nodes and e is the number of edges
# O(v + e) space - where v is the number of nodes and e is the number of edges
from collections import deque

class Solution:
    def findTrees(self, nodes, edges):
        if nodes <= 0:
            return []

        # with only one node, since its in-degrees will be 0,
        # therefore, we need to handle it separately
        if nodes == 1:
            return [0]

        # initialize the graph
        in_degrees = {i: 0 for i in range(nodes)}
        graph = {i: [] for i in range(nodes)}

        # build the graph
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            # since this is an undirected graph, therefore, add a link for both the nodes
            graph[n1].append(n2)
            graph[n2].append(n1)
            # increment the in-degrees of both the nodes
            in_degrees[n1] += 1
            in_degrees[n2] += 1

        # find all leaves i.e., all nodes with 1 in-degrees
        leaves = deque()
        for key in in_degrees:
            if in_degrees[key] == 1:
                leaves.append(key)

        # remove leaves level by level and subtract each leave's children's in-degrees.
        # Repeat this until we are left with 1 or 2 nodes, which will be our answer.
        # Any node that has already been a leaf cannot be the root of a minimum height tree, 
        # because its adjacent non-leaf node will always be a better candidate.
        total_nodes = nodes
        while total_nodes > 2:
            leaves_size = len(leaves)
            total_nodes -= leaves_size
            for _ in range(leaves_size):
                vertex = leaves.popleft()
                # get the node's children to decrement their in-degrees
                for child in graph[vertex]:
                    in_degrees[child] -= 1
                    if in_degrees[child] == 1:
                        leaves.append(child)

        return list(leaves)