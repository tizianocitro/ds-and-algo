# Ordered Set

`Ordered Set` is an extension of the `Set/HashSet` data structure.

An Ordered Set is a powerful data structure that blends the uniqueness of a set with the ordered sequence of a list. Unlike traditional sets, where the elements are unsorted, an ordered set maintains the sequence of its elements.

The primary purpose of using an ordered set is to have a collection that not only avoids duplicate elements but also preserves their order. This ordering can be either the natural ordering of the elements or defined by a custom comparator. The ordered set is particularly useful when the sequence in which data is processed or retrieved is crucial.

## What is a Set/HashSet?

A `HashSet` is a collection or a group of unique elements. Think of it as a party where everyone has a different name; no two people can have the same name. In coding terms, this means HashSets do not allow duplicate values.

### HashTable vs HashSet

`HashTable` is like a dictionary, full of word (key) and definition (value) pairs. In contrast, `HashSet` is more like a unique-word collector, not bothered about definitions, just the words.

![HashTable vs HashSet](/assets/hashtable_vs_hashset.png "HashTable vs HashSet")

### Core Characteristics of HashSets

- **Uniqueness**: The first thing to remember about HashSets is that every element is unique. It’s like having a basket of fruits, and no two fruits in it are the same.
- **Null Elements**: A HashSet can include a null element. It’s like having an empty slot in your fruit basket, and that’s perfectly okay.
- **Order**: When it comes to order, HashSets like to keep it casual. They do not guarantee any specific order of the elements. It’s like reaching into your fruit basket blindfolded – you never know which fruit you’ll grab first.

### Internal Working of a HashSet

- **Handling Duplicates**: So, what happens when HashSets encounter a duplicate? They simply ignore it! If you try to add a fruit that’s already in your basket, HashSet will just keep the original and discard the duplicate.
- **Hashing Function**: HashSets, like HashTables, use a hashing function to decide where each element should go. It’s like assigning a specific spot in your basket for each fruit based on its name.
**Resizing the Set**: What happens when your basket gets full? When a HashSet starts running out of room, they increase the basket size to make space for more unique elements.

## Ordered Set vs Set

The primary difference between a standard set and an ordered set is the element ordering. In a regular set, elements are stored with no particular order, and iterating over a set does not guarantee the order in which elements are returned. In contrast, an ordered set maintains its elements in a sorted order, whether it's natural ordering or a specified one.

The ordered set can perform all operations performed by the set data structure. Additionally, it can perform below two operations in `O(logN)` time.

1. `find_by_order(k)`: it efficiently retrieves the `kth element` in the set, measured from zero, in `O(logN)` time. It's a game-changer for direct access based on element order. For example, in a set `{1, 5, 6, 17, 88}`:
    - `find_by_order(2)` fetches the `3rd element` in the set, which is `6`
    - `find_by_order(4)` accesses the `5th element` in the set, i.e., `88`

2. `order_of_key(k)`: This operation determines the number of elements in the set that are strictly smaller than the specified element `k`, also in `O(logN)` time. It's a quick way to gauge the position of an element in the sorted order. Considering the same set `{1, 5, 6, 17, 88}`:
    - `order_of_key(6)` reveals that `2` elements are smaller than `6`.
    - `order_of_key(25)` shows that `4` elements are smaller than `25`.

These advanced functions extend the capabilities of ordered sets, making them a more robust and versatile choice compared to traditional sets, especially in scenarios requiring both order-sensitive and unique data management.

## Practical Applications of Ordered Set with Examples

Ordered sets can be used in scenarios where data is constantly updated and specific range-based queries are required. Let's explore some examples to demonstrate the utility of ordered sets in managing dynamic data sets and executing range queries effectively.

### Example 1: Managing and Querying a Dynamically Updated Array

Imagine a system where data elements are continuously added to an array. After each new addition, a query is made to find out how many elements within the array fall between a specified range (`[l, r]`). Initially, the array is empty.

#### Role of an Ordered Set

In such a situation, an ordered set is crucial. It can keep the elements in a sorted sequence as they are added, facilitating quick and accurate range queries.

To illustrate, let's look at the below example:

```python
Input: 5
       [1, 2]
       1
       [2, 5]
       2
       [1, 5]

Output: 0
        1
        3
```

**Explanation**:
- The array starts off as empty.
- Post inserting `5`, the query for range `[1, 2]` yields no matching elements.
- On adding `1`, within the range `[2, 5]`, the element `5` meets the criteria.
- With `2` added, all elements `(1, 2, 5)` fall within the queried range `[1, 5]`.

Through this example, the ordered set's ability to manage and query data in a dynamic environment is evident. Its ordered nature allows for efficient calculation of element counts within specific ranges, showcasing its practicality in scenarios with frequent data updates and the need for immediate, accurate range-based information.

### Example 2: User Activity Logs

Imagine an application that maintains a log of user activities. An ordered set can be used to keep these logs in a chronological sequence without any duplicates, ensuring efficient data retrieval in the exact order of occurrence.

## Implementing an Ordered Set

Here's is the implementation in Python:

```python
class OrderedSet:
    def __init__(self):
        self.set = []

    def add(self, element):
        if element not in self.set:
            self.set.append(element)
            self.set.sort(reverse=True)

    def find_by_order(self, k):
        if k < 0 or k >= len(self.set):
            return None
        return self.set[k]

    def order_of_key(self, element):
        return sum(1 for x in self.set if x > element)
```

### Time and Space Complexity Analysis

- **Time complexity**: The time complexity for common operations like addition, removal, and searching in a **TreeSet** is `O(logN)`, where `N` is the number of elements in the set. This is because `TreeSet` is typically implemented using a tree structure.
- **Space complexity**: The space complexity is `O(N)`, as it needs to store each unique element.