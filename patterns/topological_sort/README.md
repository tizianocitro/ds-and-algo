# Topological Sort

Topological Sort is used to find a linear ordering of elements that have dependencies on each other. For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.

## Idea

The basic idea behind the topological sort is to provide a partial ordering among the vertices of the graph such that if there is an edge from `U` to `V` then `U <= V` i.e., U comes before V in the ordering.

Here are a few fundamental concepts related to topological sort:

1. *Source*: Any node that has no incoming edge and has only outgoing edges is called a source.
2. *Sink*: Any node that has only incoming edges and no outgoing edge is called a sink.
3. A topological ordering starts with one of the sources and ends at one of the sinks.
4. A topological ordering is **possible only when the graph has no directed cycles**, i.e. if the graph is a `Directed Acyclic Graph (DAG)`. If the graph has a cycle, some vertices will have cyclic dependencies which makes it impossible to find a linear ordering among vertices.

To find the topological sort of a graph we can traverse the graph in a **Breadth First Search (BFS)** way. We will start with all the sources, and in a stepwise fashion, save all sources to a sorted list. We will then remove all sources and their edges from the graph. After the removal of the edges, we will have new sources, so we will repeat the above process until all vertices are visited.

Here is the visual representation of this algorithm:

![Visual representation of the algorithm](/assets/topological_sort.png "Visual representation of the algorithm")

## Algorithm

This is how we can implement this algorithm:

1. **Initialization**:

    1. We will store the graph in **Adjacency Lists**, which means each parent vertex will have a list containing all of its children. We will do this using a **HashMap** where the `key` will be the parent vertex number and the value will be a List containing children vertices.
    2. To find the sources, we will keep a **HashMap to count the in-degrees** i.e., count of incoming edges of each vertex. Any vertex with `0` in-degree will be a source.

2. **Build the graph and find in-degrees of all vertices**: We will build the graph from the input and populate the in-degrees HashMap.

3. **Find all sources**: All vertices with `0` in-degrees will be our sources and we will store them in a **Queue**.

4. **Sort**:
    1. For each source, do the following things:
        1. Add it to the sorted list.
        2. Get all of its children from the graph.
        3. Decrement the in-degree of each child by `1`.
        4. If a child’s in-degree becomes `0`, add it to the sources Queue.
    2. Repeat step 1, until the source Queue is empty.

## Code

```python
from collections import deque

class Solution:
    def sort(self, vertices, edges):
        sorted_order = []
        if vertices <= 0:
            return sorted_order

        # initialization
        # count of incoming edges
        in_degree = {i: 0 for i in range(vertices)}
        # adjacency list graph
        graph = {i: [] for i in range(vertices)}

        # build the graph
        for edge in edges:
            parent, child = edge[0], edge[1]
            # put the child into it's parent's list
            graph[parent].append(child)
            # increment child's in_degree
            in_degree[child] += 1

        # find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

        # for each source, add it to the sorted_order and subtract '1
        # from all of its children's in-degrees if a child's in-degree
        # becomes zero, add it to sources queue
        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)
            # get the node's children to decrement their in-degrees
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                sources.append(child)

        # topological sort is not possible as the graph has a cycle
        if len(sorted_order) != vertices:
            return []

        return sorted_order
```

## Complexity

**Time Complexity**: In step `d`, each vertex will become a source only once and each edge will be accessed and removed once. Therefore, the time complexity of the above algorithm will be `O(V+E)`, where `V` is the total number of vertices and `E` is the total number of edges in the graph.

**Space Complexity**: The space complexity will be `O(V+E)`, since we are storing all of the edges for each vertex in an adjacency list.

