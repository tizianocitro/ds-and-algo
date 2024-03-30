# Graph

A graph is a data structure that consists of a set of vertices (nodes) and a bunch of edges connecting these vertices. Graphs are widely used to model real-world scenarios where relationships and connections between entities must be represented. For example, a Graph `G = (V, E)` can five vertices `V = (A, B, C, D, E)` and six edges `E = ((A, B), (B, C), (C, E), (E, D), (D, B), (D, A))`.

Graphs can become more complex as they grow and have many interconnected nodes and edges. Graphs are a fundamental and versatile data structure used in various computer science applications to model and solve complex problems involving relationships and connections.

## Application of Graphs

Graphs are versatile data structures that find applications in various fields. Here are five graph applications with facts and figures:

1. **Social Network Analysis**: Graphs are widely used for analyzing social networks to understand connections between individuals or entities.

2. **Transportation Network Optimization**: Graphs are crucial in optimizing transportation networks like road or flight routes. For example, the road network of the United States spans over 4 million miles. Using graph algorithms like Dijkstra's algorithm, authorities can efficiently find the shortest path between two locations, minimizing travel time and fuel consumption.

3. **Internet and Webpage Ranking**: Search engines like Google use graphs to rank webpages and determine their relevance to a search query. Google's PageRank algorithm utilizes a graph representation of the web.

4. **Recommendation Systems**: Graphs are employed in recommendation systems to provide personalized suggestions to users based on their preferences and behaviors. A popular streaming platform, Netflix uses a graph-based collaborative filtering approach to recommend movies and TV shows to its subscribers.

5. **Bioinformatics and Protein Interactions**: In bioinformatics, graphs model complex biological interactions, such as protein-protein interactions, gene regulatory networks, and metabolic pathways. The Human Protein Reference Database (HPRD), which stores protein-protein interaction data, contains information about more than 39,000 interactions among over 9,000 proteins.

These examples demonstrate the wide-ranging applications of graphs in different domains, each significantly impacting the respective industries.

## Common Graph Terminologies

Understanding baseline graph terminologies is essential for understanding complex graph concepts. Like the other concepts, graph theory has some baseline terminologies. These terminologies are the most commonly used jargon in graphs.

Here are some of the most commonly used graph terminologies.

### Digraph

A digraph, short for directed graph, is a type of graph in which edges have a direction or are represented by arrows. Each edge connects two vertices (nodes), but the direction of the edge indicates a one-way relationship between the nodes. In other words, if there is an edge from vertex `A` to vertex `B`, you can only travel from `A to B` along that edge.

![Digraph](/assets/digraph.png "Digraphs")

### Loop in Graph

A loop in a graph refers to an edge that connects a vertex to itself. In other words, it is an edge that starts and ends at the same vertex. Loops can exist in both directed and undirected graphs.

In an undirected graph, a loop is simply an edge that connects a vertex to itself. It forms a cycle of length `1`. For example, if you have a graph with a single vertex `V`, and there is an edge from `V` to itself, then it forms a loop.

![Loop in undirected graph](/assets/loop_in_undirected_graph.png "Loop in undirected graphs")

In a directed graph, a loop is an arc (directed edge) that starts and ends at the same vertex. It forms a directed cycle of length `1`. For example, if you have a graph with a single vertex `v`, and there is a directed edge from `V` to itself, then it forms a loop.

![Loop in directed graph](/assets/loop_in_directed_graph.png "Loop in directed graphs")

### Node in Graph

A node (also known as a vertex) is a fundamental building block of a graph. A graph is a mathematical representation of a set of vertices (nodes) and the connections (edges) between those objects. The links between nodes can be either directed or undirected, depending on whether the relationship has a specific direction. In the following figure, `A, B, C, D, and E` are the nodes in the graph, also known as vertices.

![Node in graph](/assets/node_in_graph.png "Node in graph")

### Adjacent Nodes

Two nodes are said to be adjacent (neighbor) if an edge is connecting them directly. The set of nodes adjacent to a particular node is known as its neighborhood. As in the above figure, the nodes `A` and `B` are adjacent.

### Degree of a Node

The degree of a node is the number of edges connected to it. In an undirected graph, it represents the number of neighbors a node has. As in the above figure, the degree of Node A is two because it has two neighbors.

In a directed graph, there are two degrees:

- The in-degree (number of incoming edges).
- The out-degree (number of outgoing edges).

![Degree of nodes](/assets/degree_of_nodes.png "Degree of nodes")

In the above graph, the out-degree of node `A` is two because two edges are outgoing, and the in-degree and out-degree of node `C` is `1` because it has one incoming and one outgoing edge.

### Path

A sequence of vertices in which each consecutive pair of vertices is connected by an edge. For example in the above figure, there is a path from vertex `A to B`.

### Cycle

A path in which the first and last vertices are the same, forming a closed loop. The following figure shows a route from `A to B`, `B to D`, `D to C`, and `C to A`. So here, the cycle completes because we start from vertex A and end again at A vertex.

![Cycle](/assets/cycle.png "Cycle")

## Graph Types

There are several types of graphs, each with its specific characteristics. Here are some common types of graphs, along with examples:

1. **Undirected Graph**: In an undirected graph, edges have no direction, representing a bidirectional connection between two vertices. If an edge exists between vertex `A` and vertex `B`, you can traverse from `A to B` and vice versa. *Example*: Friends Network.

    ![Undirected Graph](/assets/undirected_graph.png "Undirected Graph")

2. **Directed Graph**: In a directed graph, edges have a direction, indicating a one-way connection between vertices. If there is an edge from vertex `A` to vertex `B`, you can only traverse from `A to B`, not vice versa. *Example*: Webpage Links.

    ![Directed Graph](/assets/directed_graph.png "Directed Graph")

3. **Weighted Graph**: Each edge is associated with a numerical value called a weight in a weighted graph. The weight can represent distances, costs, or any other relevant metric between the connected vertices. *Example*: Transportation Network.

    ![Weighted Graph](/assets/weighted_graph.png "Weighted Graph")

4. **Unweighted Graph**: All edges have the same default weight of `1` in an unweighted graph. There are no additional numerical values associated with the edges. In an unweighted graph, the absence of edge weights implies that all edges are considered to have equal importance or distance between the connected nodes. *Example*: Family Tree (connection exists or doesn't).

    ![Unweighted Graph](/assets/unweighted_graph.png "Unweighted Graph")

5. **Cyclic Graph**: A cyclic graph is a graph that contains at least one cycle, which is a closed path (sequence of vertices) that starts and ends at the same vertex.

    ![Cyclic Graph](/assets/cyclic_graph.png "Cyclic Graph")

6. **Acyclic Graph**: An acyclic graph is a directed graph that has no cycles. A cycle occurs when the following edges from a node lead back to the same node. Some key properties of acyclic graphs:

    - They have at least one node with no incoming edges (called a source node).
    - They have at least one node with no outgoing edges (called a sink node).

    In this graph, node `A` is the root node. It has no incoming edges. Nodes `D, E, F, G` are leaf nodes - they have no outgoing edges. There are no cycles in this graph.
    A valid topological ordering of the nodes could be:` A, B, C, D, E, F, G`. So this graph structure forms an acyclic-directed graph. **Trees** and **DAGs (Directed Acyclic Graphs)** are common examples of acyclic graph structures.

    ![Acyclic Graph](/assets/acyclic_graph.png "Acyclic Graph")

7. **Connected Graph**: A connected graph is one in which there is a path between every pair of vertices. In other words, every vertex is reachable from any other vertex in the graph.

    ![Connected Graph](/assets/connected_graph.png "Connected Graph")

8. **Disconnected Graph**: A disconnected graph has two or more connected components (subgraphs) with no direct connection between these components. The figure below is one separate graph. The first component contains `A, B, C, and D` vertices, and the other part contains `E, F, G, and H`, with at least two vertices not connected by a path.

    ![Disconnected Graph](/assets/disconnected_graph.png "Disconnected Graph")

9. **Strongly Connected Graphs**: A strongly connected graph is a type of directed graph in which there is a directed path from every vertex to every other vertex. In other words, for any two vertices, `A` and `B`, in a strongly connected graph, there is a directed path from `A to B` and `B to A`.

    ![Strongly Connected Graph](/assets/strongly_connected_graph.png "Strongly Connected Graph")

These are some of the common types of graphs in data structures. Each type has its significance and use cases depending on the problem at hand. Understanding different types of graphs is crucial for effectively applying graph algorithms and solving graph-related problems.

## Graph Representations

We primarily represent graphs using two ways:

1. Adjacency matrix
2. Adjacency list

### Adjacency Matrix

An adjacency matrix is a common way to represent a graph as a matrix. It is a square matrix where the rows and columns represent the vertices of the graph, and the entries (elements) of the matrix indicate whether there is an edge between the corresponding vertices.

In an undirected graph, the edges have no direction, meaning they can be traversed in both directions between two vertices. On the other hand, in a directed graph, the edges have a direction, indicating a one-way relationship between two vertices.

As there are two major types of graphs directed graph and undirected graph. Let's see how the adjacency matrix works for both types of graphs.

### Adjacency Matrix for Undirected Graphs

In an undirected graph with `N` vertices, the adjacency matrix `A` will be an `N x N` matrix. For an undirected edge between vertices `i` and `j`, the corresponding entries in the matrix (`A[i][j]` and `A[j][i]`) will have a value of `1`, indicating the presence of an edge. If there is no edge between vertices `i` and `j`, the matrix entries will have the value of `0`.

Considering an undirected graph with `4` vertices `(A, B, C, D)` and `4` edges `(A-B, B-C, C-D, D-A)`, the adjacency matric for the graph will be:

![Adjacency Matrix for Undirected Graphs](/assets/adjacency_matrix_undirected.png "Adjacency Matrix for Undirected Graphs")

### Adjacency Matrix for Directed Graphs

In a directed graph with `N` vertices, the adjacency matrix `A` will also be an `N x N` matrix. For a directed edge from vertex `i` to vertex `j`, the corresponding entry in the matrix (`A[i][j]`) will have the value of `1`, indicating the presence of an edge from `i` to `j`. If there is no edge from vertex `i` to vertex `j`, the matrix entry (`A[i][j]`) will have the value of `0`.

Considering of a directed graph with `4` vertices `(A, B, C, D)` and `5` directed edges `(A->B, A->C, C->D, D->B, D->C)`, the adjacency matric for the graph will be:

![Adjacency Matrix for Directed Graphs](/assets/adjacency_matrix_directed.png "Adjacency Matrix for Directed Graphs")

The above figure explains the adjacency matrix of the directed graph in such a way that there is an edge between vertices `A-C` and `A-B` so `1` is placed there.

### Adjacency List

An adjacency list is a common way to represent the connections between vertices in a graph. It is used in both directed and undirected graphs, but the way edges are stored and described differs slightly between the two types. In an adjacency list, each vertex is associated with a list of its neighboring vertices directly connected to it.

### Adjacency List for Undirected Graphs

In an undirected graph, the edges between vertices have no direction. If vertex `A` is connected to vertex `B`, then vertex `B` is also connected to vertex `A`. As a result, the adjacency list for an undirected graph is symmetric. Here is an example of an adjacency list for an undirected graph with `4` vertices `(A, B, C, D)` and `4` edges `(A-B, B-C, C-D, D-A)`.

![Adjacency List for Undirected Graphs](/assets/adjacency_list_undirected.png "Adjacency List for Undirected Graphs")

From vertex `A` there is an edge to vertex `B` and `C` in the graph. So in the adjacency list, there are two nodes from node `A`.

### Adjacency List for Directed Graphs

In a directed graph, the edges between vertices have a direction. If vertex `X` is connected to vertex `Y`, it does not necessarily mean that vertex `Y` is connected to vertex `X`. As a result, the adjacency list for a directed graph is not symmetric.

Here is an example of adjacency list for a directed graph with `4` vertices `(A, B, C, D)` and `4` directed edges `(A->B, A->C, C->D, D->B)`:

![Adjacency List for Directed Graphs](/assets/adjacency_list_directed.png "Adjacency List for Directed Graphs")

From vertex `A` there is an edge to vertex `B` and `C` in the graph. So in the adjacency list, there are two nodes from node `A`. From vertex `B` there is no edge coming out so the adjacency list contains no further node from node `B`.

## Graph as an Abstract Data Type (ADT)

An `Abstract Data Type (ADT)` is a theoretical concept that defines a set of operations and their behavior without specifying the internal representation of the data or the algorithms used to implement those operations. It provides a high-level description of the data and the functions that can be performed on it.

Here are some of the operations can be performed on graphs:

- Adding a new vertex
- Removing a vertex
- Adding an edge between two vertices
- Removing an edge between two vertices
- Getting a list of all the vertices
- Checking if two graph nodes are adjacent to each other or not
- Getting count of the total vertices in the graph
- Getting count of the total edges in the graph
- Getting a list of the graph edges
- Getting neighbors of a graph vertex

There are a few other ADT operations involving graph searching and traversal.

```python
class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def add_vertex(self, vertex):
        pass # Add a new vertex to the graph.

    def remove_vertex(self, vertex):
        pass # Remove a vertex from the graph.

    def add_edge(self, vertex1, vertex2):
        pass # Add an edge between two vertices.

    def remove_edge(self, vertex1, vertex2):
        pass # Remove an edge between two vertices.

    def get_vertices(self):
        return [] # Get a list of all vertices.

    def is_adjacent(self, vertex1, vertex2):
        return False # Check if two vertices are adjacent.

    def get_vertex_count(self):
        return 0 # Get the total number of vertices.

    def get_edge_count(self):
        return 0 # Get the total number of edges.

    def get_edges(self):
        return [] # Get a list of all edges.

    def get_neighbors(self, vertex):
        return [] # Get a list of neighbors of a given vertex.
```

### Implementing the ADT operations

Let's understanding how some the operations are implemented.

#### Adding a New Vertex

The function `add_vertex(vertex)` is a common operation in graph theory, where it adds a new vertex (also called a node or point) to a graph data structure. The vertex is a fundamental unit of a graph and represents an entity or an element. Adding a vertex expands the graph and creates potential connections (edges) between this new vertex and existing vertices.

In an adjacency list, each vertex is associated with a list of its adjacent vertices. We are using a dictionary or map for implementing the adjacency list. Thereby, we are able to store node key and value(s) associated with it.

In this implementation, we assume that a graph doesn't have any extra satellite data or values associated with it. Therefore, we will add an empty vector or list as a value attribute for the new graph node or vertex.

Adding a new vertex involves the following two main steps:

- Check if vertex already exists, using predefined map or dictionary search methods.
- If not, add it by inserting a new key-value pair. Keep value of the new inserted vertex as empty list.

Here is a generalized pseudocode:

```text
Graph is represented as:

adjacencyList (map/dictionary):
  key: vertex 
  value: list of adjacent vertices

Function addVertex(vertex)

  if vertex does not exist in adjacencyList

    add new key-value pair:
      key: vertex
      value: empty list     
    end if

end Function
```

```python
def add_vertex(self, vertex):
  if vertex not in self.adjacency_list:
    self.adjacency_list[vertex] = []
```

#### Adding an Edge between Two Vertices

Pseudocode:

```text
Function addEdge(vertex1, vertex2):

  insert vertex2 into adjacencyList[vertex1]
  insert vertex1 into adjacencyList[vertex2]

end Function
```

To implement the `add_edge()` function, we need to add an edge between `vertex1` and `vertex2` in the graph. Here is the implementation:

```python
def add_edge(self, vertex1, vertex2):
    self.adjacency_list[vertex1].append(vertex2)
    self.adjacency_list[vertex2].append(vertex1)
```

### A Complete Graph ADT Implementation

```python
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return 
        self.adjacency_list.pop(vertex)
        for neighbors in self.adjacency_list.values():
            if vertex in neighbors:
                neighbors.remove(vertex)

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
        
    def get_vertices(self):
        return list(self.adjacency_list.keys())
        
    def get_edges(self):
        edges = []
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                if vertex < neighbor:
                    edges.append((vertex, neighbor))
        return edges
    
    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def is_adjacent(self, vertex1, vertex2):
        return vertex2 in self.adjacency_list[vertex1]
    
    def get_vertex_count(self):
        return len(self.adjacency_list)
    
    def get_edge_count(self):
        count = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        return count // 2 # Divide by 2 because otherwise we would count every edhe two times.
```

## Graph Traversal

A graph consists of vertices (nodes) connected by edges (lines). Graph traversal involves visiting all the graph nodes following a specific strategy or order. During traversal, each node is typically marked as visited to avoid revisiting the same node multiple times and to prevent infinite loops in cyclic graphs.

There are two common graph traversal algorithms: **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**.

## Depth-First Search (DFS)

Depth-First Search (DFS) is a graph traversal algorithm that explores all the nodes in a graph by systematically visiting as far as possible along each branch before backtracking. It operates on both directed and undirected graphs and can be implemented using recursion or an explicit stack data structure.

DFS starts from a selected source node (or a starting point) and explores as deeply as possible along each branch before backtracking. The algorithm visits nodes in a depth ward motion until it reaches a leaf node with no unexplored neighbors. At that point, it backtracks and explores other unexplored branches.

DFS can be used for various applications, such as finding connected components, detecting cycles in the graph, topological sorting, and solving problems like maze exploration or finding paths between nodes.

It's essential to be cautious about infinite loops when traversing graphs that may have cycles. To avoid this, the algorithm must keep track of visited nodes and avoid revisiting nodes that have already been explored.

Overall, DFS is a powerful graph traversal algorithm that can efficiently explore the entire graph and is widely used in many graph-related problems.

Here's a step-by-step explanation of the DFS algorithm:

1. **Initialization**:

    - Choose a starting node as the source node.
    - Create a data structure to keep track of visited nodes (e.g., an array or a hash set) and mark the source node as visited.

2. **Visit the Current Node**: process the current node (e.g., print its value or perform any other operation you need to do).

3. **Recursive Approach (Using Recursion)**: ror each unvisited neighbor of the current node recursively call the DFS function with the neighbor as the new current node.
Mark the neighbor as visited.

4. **Stack-Based Approach (Using an Explicit Stack)**:

    - Push the starting node onto the stack.
    - While the stack is not empty:
        - Pop a node from the stack (current node).
        - Process the current node (e.g., print its value or perform any other operation you need to do).
        - For each unvisited neighbor of the current node:
            - Push the unvisited neighbor onto the stack.
            - Mark the neighbor as visited.

5. **Backtracking**: if there are no more unvisited neighbors for the current node, backtrack by returning from the recursive function (if recursion) or popping nodes from the stack until a node with unvisited neighbors is found (if using an explicit stack).

6. **Termination**: the DFS algorithm terminates when all nodes reachable from the source node have been visited. This means that all connected components of the graph have been explored.

### Example of DFS on Graph

Consider the following graph:

![DFS on Graph](/assets/dfs_graph.png "DFS on Graph")

Starting from node `A`, let's perform DFS on this graph:

1. Start at node A (the source node).
2. Mark node A as visited and process it: A (visited).
3. Explore an unvisited neighbor of A. Let's say we choose B.
4. Mark node B as visited and process it: A -> B (visited).
5. From node B, explore an unvisited neighbor. We choose D.
6. Mark node D as visited and process it: A -> B -> D (visited).
7. Node D has no unvisited neighbors, so we backtrack to node B.
8. Node B has another unvisited neighbor, E. We explore E.
9. Mark node E as visited and process it: A -> B -> D -> E (visited).
10. From node E, explore an unvisited neighbor. We choose F.
11. Mark node F as visited and process it: A -> B -> D -> E -> F (visited).
12. Node F has no unvisited neighbors, so we backtrack to node E.
13. Node E has no more unvisited neighbors, so we backtrack to node B.
14. Node B has no more unvisited neighbors, so we backtrack to node A.
15. Node A has one more unvisited neighbor, C. We explore C.
16. Mark node C as visited and process it: A -> B -> D -> E -> F -> C (visited).
17. Node C has no unvisited neighbors, so we backtrack to node A.
18. Node A has no more unvisited neighbors, and we have visited all reachable nodes.

The DFS traversal order for this graph starting from node `A` is: `A -> B -> D -> E -> F -> C`.

*Note that the choice of the starting node can affect the order of traversal for the graph. Also, in a disconnected graph, you would need to start DFS from each unvisited node to traverse all components*.

### Implementation of DFS

In this example implementation, we assume that the graph is represented as an adjacency list.

```python
class Graph:
    def __init__(self, V):
        self.vertices = V
        self.adjList = [[] for _ in range(V)]

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)  # For an undirected graph

    def DFS(self, start):
        visited = [False] * self.vertices
        stack = []

        stack.append(start)
        visited[start] = True

        while stack:
            curr = stack.pop()
            print(curr)

            # Without the reversed() it traverses the right branches before the left ones
            # for neighbor in reversed(self.adjList[curr]):
            for neighbor in self.adjList[curr]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
```

### Complexity Analysis of DFS

The time and space complexity of Depth-First Search (DFS) depend on the size and structure of the graph being traversed. Let's analyze the complexity of DFS:

#### Time Complexity

In the worst case, DFS once visits all nodes and edges in the graph. For a graph with `V` vertices (nodes) and `E` edges, the time complexity of DFS is `O(V + E)`.

The time complexity can be further broken down as follows:

- Visiting a node (marking it as visited and processing it) takes `O(1)` time.
- Exploring all neighbors of a node takes `O(d)` time, where `d` is the average degree of nodes in the graph. In the worst case, `d` can be as high as `V - 1` (complete graph).
- So, the time complexity can be approximated as `O(V)` for exploring all neighbors of one node.

In summary, the overall time complexity of DFS is `O(V + E)`.

#### Space Complexity

The space complexity of DFS is determined by the space needed to store information about the nodes during the traversal. The primary sources of space usage are the *recursion stack* (if using recursion) or the *explicit stack data structure* (if using an iterative approach).

In the worst case, the maximum depth of the recursion stack (or the maximum number of nodes stored in the stack) is the height of the deepest branch of the graph. For a graph with a single connected component, this height can be `O(V - 1)` (when all nodes are connected in a straight line).

The space complexity of the recursion stack in the worst case is `O(V)`. Similarly, if an explicit stack is used, its space complexity would also be `O(V)` in the worst case.

In summary, the overall space complexity of DFS is `O(V)` due to the recursion stack or the explicit stack.

## Breadth-First Search (BFS)

Breadth-First Search (BFS) is a graph traversal algorithm that explores a graph's vertices (nodes) level by level. It starts from a selected source node and moves outward to visit all the nodes at the same distance from the source before moving on to nodes at the following distance level.

BFS is particularly useful for finding the shortest path in unweighted graphs and for systematically exploring graphs.

BFS is generally efficient for searching and traversal when the graph is not too dense. For sparse graphs, where `E` is much smaller than `V^2`, the time complexity becomes almost linear, making BFS a reasonable choice for many practical applications.

BFS guarantees it visits nodes according to their distance from the source node. It is an efficient algorithm to find the shortest path in unweighted graphs. Additionally, BFS can find connected components, detect cycles, and solve graph-related problems. However, it may consume more memory than DFS, especially in graphs with a significant or infinite branching factor.

Here is a complete description of the Breadth-First Search algorithm:

1. **Usage of a Queue**: BFS uses a queue to keep track of the nodes to be visited. The queue follows the First-In-First-Out (FIFO) principle, where the first node inserted in the queue will be the first one to be removed (dequeue).

2. **Initialization**:

    - Start by selecting a source node to begin the traversal.
    - Create an empty queue to hold the nodes to be visited.
    - Mark the source node as visited and enqueue it into the queue.

3. **Traversal**: while the queue is not empty, continue the following steps:

    - Dequeue a node from the front of the queue (let's call it the "current node").
    - Process the current node (print it, perform some operation, etc.).
    - Enqueue all the unvisited neighbors of the current node into the queue.
    - Mark each enqueued neighbor as visited.

4. **Termination**: the BFS algorithm continues until the queue becomes empty, meaning all reachable nodes from the source node have been visited.

### Example of BFS on Graph

Consider the following graph:

![BFS on Graph](/assets/bfs_graph.png "BFS on Graph")

Starting from the source node `A`, the BFS traversal would be as follows:

1. Start with A (the source node) and enqueue it. *Queue*: [A]
2. Dequeue A and process it. Enqueue its neighbors B and C. *Queue*: [B, C]
3. Dequeue B and process it. Enqueue its neighbors D and E. *Queue*: [C, D, E]
4. Dequeue C and process it. Enqueue its neighbor F. *Queue*: [D, E, F]
5. Dequeue D and process it. No unvisited neighbors to enqueue. *Queue*: [E, F]
6. Dequeue E and process it. Enqueue its neighbor F. *Queue*: [F]
7. Dequeue F and process it. No unvisited neighbors to enqueue. *Queue*: []

The BFS traversal order is: `A -> B -> C -> D -> E -> F`.

BFS guarantees that it visits nodes in the order of their distance from the source node.

### Implementation of BFS

BFS is an algorithm used for traversing or searching a graph or tree in a level-by-level manner.

```python
from collections import deque

class Graph:
    def __init__(self, V):
        self.vertices = V
        self.adjList = [[] for _ in range(V)]

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)  # For an undirected graph

    def DFS(self, start):
        visited = [False] * self.vertices
        queue = deque()

        queue.append(start)
        visited[start] = True

        while queue:
            curr = queue.popleft()
            print(curr)

            for neighbor in self.adjList[curr]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
```

### Complexity Analysis of BFS

The time and space complexity of Breadth-First Search (BFS) depends on the size of the graph and the way it is represented.

#### Time Complexity

- Visiting a vertex takes `O(1)` time as we dequeue it from the queue in constant time.
- Exploring the neighbors of a vertex takes `O(1)` time per neighbor, as we have to traverse its adjacency list once.
- In the worst case, we visit all the vertices at least once, which takes `O(V)` time. Additionally, for each vertex, we explore all its neighbors once, which takes `O(E)` time in total (sum of the sizes of all adjacency lists).
- Hence, the overall time complexity of BFS is: `O(V + E)`.

#### Space Complexity

- The space required to store the graph using an adjacency list representation is `O(V + E)`, as we need to store each vertex and its corresponding edges.
- The space required for the queue in BFS is `O(V)` in the worst case, as all the vertices can be in the queue at once.
- Since the space occupied by the queue is dominant in the overall space complexity, the space complexity of BFS is: `O(V)`.
