# Union Find

Union Find, also known as **Disjoint Set Union (DSU)**, is a data structure that keeps track of a partition of a set into disjoint subsets (meaning no set overlaps with another). It provides two primary operations: **find**, which determines which subset a particular element is in, and **union**, which merges two subsets into a single subset. This pattern is particularly useful for problems where we need to find whether 2 elements belong to the same group or need to solve connectivity-related problems in a graph or tree.

## Core Operations of Union-Find (Disjoint Set Union - DSU)

1. **Find**: Determine which set a particular element belongs to. This can be used for determining if two elements are in the same set.
2. **Union**: Merge two sets together. This operation is used when there is a relationship between two elements, indicating they should be in the same set.

## Union-Find: A Story of Connections

Imagine a social network where everyone is initially a single user with no friends. The moment two users become friends, they form a group. If a user befriends someone from another group, the two groups merge into a larger friend circle. Union-Find helps track these friendships and circles.

## How DSU Work?

1. **Initial State**: Everyone is in their own separate group. Think of each person as their own little island.
2. **Making Connections (Union)**: When two people shake hands, they now belong to the same group. If they were already in groups, their entire groups merge.
3. **Checking Connections (Find)**: Want to know if two people are connected? Union-Find can check if they're in the same group.

## How DSU is Implemented?

- **Parents Array**: Each element has a parent. In the beginning, each element is their own parent.
- **Find Operation**: Follows the chain of parents until it reaches the root parent, which represents the group.
- **Union Operation**: Connects two groups by setting the parent of one group’s root to the other group’s root.

## Naive Implementation of Disjoint Set

### Creating Disjoint Sets

- Each element points to a parent.
- Initially, each element is its own parent, forming `n` disjoint sets.
- A `root` element is one that points to itself, identifying the set's representative.

![Initial State](/assets/union_find_initial_state.png "Initial State")

```python
# initialize 'n' elements where each element is its own parent,
# 'n' is the number of elements
parent = [i for i in range(n)]
```

### Find Operation

The **Find** operation determines which set a particular element belongs to. This can be used to determine if two elements are in the same set.

In the below code:

- `parent` is an array where `parent[i]` is the parent of `i`.
- If `parent[i] == i`, then `i` is the root of the set and hence the representative.
- The `find` function follows the chain of parents for `i` until it reaches the root.

```python
def find(i):
    # if the element is its own parent, it's the representative of its set
    if parent[i] == i:
        return i
    # otherwise, recursively find the representative of the set
    return find(parent[i])
```

Above function recursively traverses the `parent` array until it finds a node that is the parent of itself.

#### Complexity Analysis

- **Time Complexity**: In the naive implementation, the time complexity of the find operation is `O(N)`, where `N` is the number of elements. This is because, in the worst case, when all elements are in the same set, we may have to traverse up to `N` elements to find the representative.
- **Space Complexity**: The space complexity of the find operation is `O(1)`  since it uses a constant amount of extra space.

### Union Operation

The `Union` operation merges two disjoint sets. It takes two elements as input, finds the representatives of their sets using the `Find` operation, and finally merges the two sets.

![Union Operation](/assets/union_find_union.png "Union Operation")

In the code below:

- **Find the Representatives**:

    - `irep = find(i)` - Finds the representative (root) of the set containing element `i`.
    - `jrep = find(j)` - Finds the representative (root) of the set containing element `j`.

- **Check if They Are in the Same Set**:

    - `if irep == jrep: return` - If `i` and `j` have the same representative, they are already in the same set, so no union is needed.

- **Merge the Sets**:

    - `parent[irep] = jrep` - Makes the representative of `i`'s set point to the representative of `j`'s set, merging the two sets.

```python
def union(i, j):
    # find the representatives of the two sets
    irep = find(i)
    jrep = find(j)

    # if they are already in the same set, return
    if irep == jrep:
        return

    # make the representative of the first set point to the representative of the second set
    parent[irep] = jrep
```

The above function merges two sets by making the representative of one set the parent of the other.

#### Complexity Analysis

- **Time Complexity**: The time complexity of the `Union` operation is dominated by the time complexity of the `Find` operation, making it `O(N)` in the worst case.
- **Space Complexity**: The space complexity of the `Union` operation is `O(1)` as it uses a constant amount of extra space.

## Optimizations

There are various methods for optimally performing operations on disjoint sets.

## Path Compression

**Path compression** is a technique used in the **Union-Find** data structure to **flatten** the structure of the tree whenever the `find` operation is called. This optimization significantly reduces the time complexity of the `find` operation, making subsequent operations faster.

The idea is to make each node on the path from a node to the root point directly to the root. This way, whenever we perform a `find` operation, we not only find the root but also make the structure flatter, which helps in reducing the depth of the trees.

Here’s how path compression works:

- When we call `find` on a node, we recursively traverse its `parent` until we reach the root.
- During this traversal, we make each node on the path point directly to the root.

![Union Find with Path Compression](/assets/union_find_path_compression.png "Union Find with Path Compression")

In the above diagram, we see a tree structure before and after path compression. Let's explain the process with an example.

1. Before Path Compression:

    - Consider we have elements connected as a tree structure.
    - Suppose we need to find the root of element `F`. The path is `F -> E -> C -> B -> A`.

2. During Path Compression:

    - As we perform the `find` operation on element `F`, we recursively move up to the root (element `A`).
    - During this traversal, we make each node (`F`, `E`, `C`, and `B`) point directly to the root (`A`).

3. After Path Compression:

    - The tree structure is **flattened**. Now, `F`, `E`, `C`, and `B` all directly point to the root (`A`).
    - Future `find` operations on any of these nodes will be much faster as they directly point to the root.

Here is the code implementation for the `find()` method for the path compression:

```python
def find(i):
    # if i is the parent of itself
    if parent[i] == i:
        # then i is the representative of its set
        return i
    else:
        # recursively find the representative of the set that i belongs to
        result = find(parent[i])

        # path compression: directly connect i to the representative of its set
        parent[i] = result

        # return the representative
        return result
```

This modified `Find` operation ensures that every node directly points to the representative of the set, and it makes it easy to find the representative of any two elements.

### Complexity Analysis

- **Time Complexity**: With path compression, the time complexity of the find operation is reduced to `O(logN)`. This is because path compression flattens the structure of the tree, reducing the depth of the tree significantly. In each find operation, we make each node on the path point directly to the root, which decreases the depth of the tree and ensures that subsequent find operations are faster. This effectively reduces the maximum height of the tree to `O(logN)`.
- **Space Complexity**: The space complexity remains `O(1)` as the operation doesn't use the extra space.

## Union by Rank

**Union by rank** is an optimization technique used in the Union-Find data structure to keep the tree **flat** and **balanced**. In the naive approach, the trees can become **skewed**, resulting in a high time complexity for the `find` and `union` operations. Union by rank addresses this issue by always attaching the smaller tree under the root of the larger tree, thereby minimizing the height of the resulting tree.

### Why Union by Rank is Important

- **Prevents Skewed Trees**: In the naive approach, repeated union operations can result in highly unbalanced trees. This can degrade the time complexity of the find operation to `O(N)`.
- **Maintains Balanced Trees**: By attaching the smaller tree under the larger tree, union by rank ensures that the resulting tree remains balanced, keeping the operations efficient.

### How Rank is Maintained

- **Rank Array**: We maintain a `rank` array where `rank[i]` denotes the **rank (or height)** of the tree rooted at element `i`.
- **Union Operation**: When performing the union of two sets, we compare the ranks of their roots:

    - If the ranks are different, the root with the higher rank becomes the parent.
    - If the ranks are the same, we arbitrarily choose one root to be the parent and increment its rank by `1`.

![Union Find with Union By Rank](/assets/union_find_union_by_rank.png "Union Find with Union By Rank")

In the above diagram, the rank of the `s1` tree is `3`, and the `s2` tree is `2`. So, the `s2` tree is connected with the `s1` tree.

```python
# Union function to merge two sets
def union_by_rank(i, j):
    # find the representative (root) of the set containing u
    irep = find(i)
    # find the representative (root) of the set containing v
    jrep = find(j)

    # if i and j are not in the same set
    if irep != jrep:
        # compare the ranks of the sets
        if rank[irep] < rank[jrep]:
            # swap i and j to ensure the larger rank is used as the new root
            swap(irep, jrep)

        # make u the parent of v (i.e., merge the sets)
        parent[jrep] = irep

        # if the ranks of the two sets were the same, increment the rank of the new root
        if rank[irep] == rank[jrep]:
            rank[irep] += 1
```

This function uses the rank array to decide which tree gets attached under which tree.

### Complexity Analysis

- **Time Complexity**: The time complexity of the `union` operation with `union by rank` is `O(logN)`. This is because `union by rank` keeps the trees balanced, ensuring that the maximum height of the tree remains logarithmic with respect to the number of elements.
- **Space Complexity**: `O(N)`, as we use the rank array.

## Union by Size

**Union by size** is another optimization technique used in the **Union-Find** data structure to keep the tree **flat** and **balanced**. Similar to `union by rank`, `union by size` helps to avoid the creation of skewed trees by always attaching the smaller tree under the larger tree. This keeps the height of the trees small, ensuring that the `find` and `union` operations remain efficient.

### How Size is Maintained

- **Size Array**: We maintain a size array where `size[i]` denotes the **size (number of elements)** of the tree rooted at element `i`.
- **Union Operation**: When performing the union of two sets, we compare the sizes of their roots:

    - If the sizes are different, the root of the smaller set becomes a child of the root of the larger set.
    - The size of the new root is updated to reflect the total number of elements in the merged set.

![Union Find with Union By Size](/assets/union_find_union_by_size.png "Union Find with Union By Size")

```python
def union_by_size(i, j):
    # find the representatives of the two sets
    irep = find(i)
    jrep = find(j)

    # if they are already in the same set, return
    if irep == jrep:
        return

    # attach the smaller tree under the larger tree
    if size[irep] < size[jrep]:
        parent[irep] = jrep
        size[jrep] += size[irep]
    else:
        parent[jrep] = irep
        size[irep] += size[jrep]
```

This function uses the size array to ensure that the tree with fewer nodes is added under the tree with more nodes.

### Complexity Analysis

- **Time Complexity**: The time complexity of the `union` operation with `union by size` is `O(logN)`. This is because `union by size` ensures that the trees remain **balanced** by attaching the smaller tree to the larger one, keeping the tree height logarithmic with respect to the number of elements.
- **Space Complexity**: `O(N)`, as we use the size array.

## Most Optimized Approach: Combining Path Compression and Union by Rank

In the previous parts, we discussed two important optimizations for the **Union-Find** data structure: **Path Compression** and **Union by Rank**. Each of these optimizations addresses specific issues related to tree depth and efficiency. By combining these two optimizations, we can achieve the **most efficient Union-Find implementation**.

## Combining Path Compression and Union by Rank

- **Path Compression**: This technique **flattens** the tree structure whenever the `find` operation is called. It does so by making each node on the path from a node to the root point directly to the root. This significantly reduces the depth of the tree, ensuring that subsequent `find` operations are faster.
- **Union by Rank**: This technique ensures that the tree remains **balanced** during `union` operations. By always attaching the smaller tree under the root of the larger tree (based on `rank`), we prevent the tree from becoming too deep. This optimization helps maintain a logarithmic tree height, keeping the operations efficient.

Combining these two optimizations, we get a highly efficient **Union-Find** structure where both the `find` and `union` operations are optimized.

### Code

To implement this combined approach, we maintain two arrays: `parent` and `rank`. The `parent` array keeps track of the parent or representative of each node, while the `rank` array helps manage the depth of the trees.

```python
class Solution:
    # initialize sets of n items
    def __init__(self, n):
        # rank: store the depth of trees (used for union by rank)
        self.rank = [1] * n
        # parent: store the parent of each item, initially, every item is its own parent
        self.parent = [node for node in range(n)]

    def find(self, x):
        # if x is not its own parent, then it's not the representative of its set
        if self.parent[x] != x:
            # path compression: connect x directly to its set's representative
            self.parent[x] = self.find(self.parent[x])
        # return the representative of the set
        return self.parent[x]

    # find the representatives (or the root nodes) for x and y
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        # if x and y are already in the same set, return
        if xset == yset:
            return

        # union by rank: attach the tree with a smaller rank under
        # the root of the tree with a larger rank
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        # if ranks are the same, choose one tree and increment its rank
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
```
### Complexity Analysis of the Most Optimized Approach

By combining **path compression** and **union by rank**, we achieve a highly efficient **Union-Find** data structure. The amortized time complexity for both `find` and `union` operations is `O(a(N))`, where `a(N)` is the **inverse Ackermann function**.

The Ackermann function grows extremely fast, and its inverse, `a(N)`, grows very slowly. For practical purposes, `a(N)` remains nearly constant, even for very large inputs.

Given this slow growth, the time complexity of the combined approach is effectively constant. Thus:

- **Time Complexity**: The amortized time complexity for `find` and `union` operations is `a(N)`, which is **nearly constant**.
- **Space Complexity**: The space complexity is `O(N)` due to the `parent` and `rank` arrays.

Combining these optimizations ensures that the **Union-Find** data structure operates efficiently, making it suitable for handling large datasets with minimal overhead.

## Pros and Cons of DSU

- *Pros*:
    - **Efficiency**: Provides near constant time operations for `union` and `find` operations, making it highly efficient.
    - **Simplicity**: Once set up, it’s straightforward to use for solving problems related to disjoint sets.
- *Cons*:
    - **Space Overhead**: Requires additional space to store the `parent` and `rank` of each element.
    - **Initial Setup**: Requires initial setup to create and initialize the data structure.

## Why Choose Union-Find Over BFS/DFS?

You can solve similar problems using the **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** algorithms, but the **Union Find** algorithm provides the optimal solution over them. For problems related to connectivity checks and component identification, **Union-Find** is often more efficient than **BFS/DFS**.

### Time Complexity Comparison

- **BFS/DFS**: For **BFS** and **DFS**, the time complexity is `O(V + E)`, where `V` is the number of vertices and `E` is the number of edges. This can be quite slow for large graphs.
- **Union-Find**: With **path compression** and **union by rank**, the amortized time complexity for `union` and `find` operations can be approximated as `O(a(N))` where `a(N)` is the inverse Ackermann function. This function grows very slowly, making **Union-Find** operations almost **constant time** in practice.
