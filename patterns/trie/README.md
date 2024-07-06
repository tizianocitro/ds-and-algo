# Trie

A **Trie**, short for retrieval, is a **specialized tree-based data structure primarily used for efficient storing, searching, and retrieval of strings over a given alphabet**.

It excels in scenarios where a large collection of strings needs to be managed and pattern-matching operations need to be performed with optimal efficiency.

## Defining a Trie

A Trie, often referred to as a `prefix tree`, is constructed to represent a set of strings where each node in the tree corresponds to a single character of a string. The path from the root node to a particular node represents the characters of a specific string. This structural characteristic allows Tries to effectively share common prefixes among strings, leading to efficient storage and retrieval.

In the context of a Trie, the given strings are typically formed from a fixed alphabet. Each edge leading from a parent node to its child node corresponds to a character from the alphabet. By following the path of characters from the root to a specific node, we can reconstruct the string associated with that path.

In the following example of a Trie, `car` and `cat` share a common prefix, and `apple` and `ant` share a common prefix.

![Trie Example](/assets/trie.png "Trie Example")

## Need for Trie Data Structure?

Tries are commonly employed in applications such as spell checking, autocomplete suggestions, and searching within dictionaries or databases. They excel at these tasks because they minimize the search complexity in proportion to the length of the target string, making them significantly more efficient than other data structures like binary search trees.

## Advantages of Using Tries

- **Fast Pattern Matching**: Tries provide rapid pattern matching queries, taking time proportional to the length of the pattern (or the string being searched).
- **Common Prefix Sharing**: Strings with common prefixes share nodes in the Trie, leading to efficient memory utilization and reduced redundancy.
- **Efficient Insertion and Deletion**: Tries are amenable to dynamic operations like insertion and deletion, while maintaining efficient search times.
- **Alphabet Flexibility**: Tries can handle various alphabets, making them versatile for a range of applications.
- **Word Frequency Counting**: Tries can be extended to store additional information at nodes, such as the frequency of words or strings.

In comparison to using a binary search tree, where a well-balanced tree would require time proportional to the product of the maximum string length and the logarithm of the number of keys, **Tries offer the advantage of a search time linearly dependent on the length of the string being searched**. This results in an optimization of search operations, especially when dealing with large datasets.

In summary, a Trie is a powerful data structure that optimizes string-related operations by efficiently storing and retrieving strings with shared prefixes. Its unique structure and fast search capabilities make it an invaluable tool in various text-based applications.

## Properties of the Trie Data Structure

Trie is a tree-like data structure. Its properties:

1. **Single Root Node**: Every trie has one root node, serving as the starting point for all strings stored within.
2. **Node as a String**: In a trie, each node symbolizes a string, with the path from the root to that node representing the string in its entirety.
3. **Edges as Characters**: The edges connecting nodes in a trie represent individual characters. This means that traversing an edge essentially adds a character to the string.
4. **Node Structure**: Nodes in a trie typically contain either hashmaps or arrays of pointers. Each position in this array or hashmap corresponds to a character. Additionally, nodes have a flag to signify if a string concludes at that particular node.
5. **Character Limitation**: While tries can accommodate a vast range of characters, for the purpose of this discussion, we're focusing on lowercase English alphabets (a-z). This means each node will have 26 pointers, with the 0th pointer representing 'a' and the 25th one representing 'z'.
6. **Path Equals Word**: In a trie, any path you trace from the root node to another node symbolizes a word or a string. This makes it easy to identify and retrieve strings.

These properties underline the essence of the trie data structure, emphasizing its efficiency and utility in managing strings, especially when dealing with large datasets.

## Implementation of Tries

Let's start by understanding the basic implementation of a Trie. Each node in a Trie can have multiple children, each representing a character. To illustrate this, consider the following simple Trie structure:

![Simple Trie Example](/assets/trie_1.png "Simple Trie Example")

Here's a step-by-step guidelines to implement a Trie:

- The Trie starts from the root node.
- The path from the root to the node "c" represents the character "c."
- The path from "c" to "a" represents the string "ca," and from "a" to "r" represents the string "car."
- The path from "c" to "a" represents the string "ca," and from "a" to "t" represents the string "cat."

## Representation of Trie Node

The Trie node has an array or list of children nodes, typically of size `26` to represent the English lowercase alphabets `(a-z)`. Additionally, there's a boolean flag `isEndOfWord` to indicate whether the current node marks the end of a word in the Trie.

![Trie Node](/assets/trie_node.png "Trie Node")

This is how it can be implemented:

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
```

Now, let's look at the basic operations such as `insertion`, `searching`, and `deletion` on the Trie data structure.

## Insertion in Trie Data Structure

Insertion in a Trie involves adding a string to the Trie, character by character, starting from the root. If the character already exists in the Trie, we move to the next node; otherwise, we create a new node for the character.

### Algorithm

1. Start from the root node.
2. For each character in the string:
    1. Check if the character exists in the current node's children.
    2. If it exists, move to the corresponding child node.
    3. If it doesn't exist, create a new node for the character and link it to the current node.
    4. Move to the newly created node.
3. After processing all characters in the string, mark the current node as the end of the word.

### Example

Consider that we need to insert the 'can', 'cat', 'cant', and 'apple' into the trie. We insert them in the following order:

1. Initial Trie: ```Root```
2. Insert 'can':
    ```
    Root
    |
    c
    |
    a
    |
    n
    ```
    *Explanation*: Starting from the root, we add nodes for each character in "can".
23. Insert 'cat':
    ```
    Root
    |
    c
    |
    a
    | \
    n   t
    ```
    *Explanation*: "cat" shares the first two characters with "can", so we just add a new branch for the 't' after 'a'.
4. Insert 'cant':
    ```
    Root
    |
    c
    |
    a
    | \
    n   t
    |
    t
    ```
    *Explanation*: "cant" extends from the path of "can", so we add a new node for 't' after the existing 'n'.
5. Insert 'apple':
    ```
    Root
    |   \
    c     a
    |     |
    a     p
    | \   |
    t   n p
    |     |
    t     l
        |
        e
    ```
    *Explanation*: Starting from the root, we add nodes for each character in "apple" branching from the 'a' node.

### Code

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # assuming only lowercase english letters
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, ch):
        # convert character to index (0-25)
        # e.g., if char = 'a' then index is 0, if char = 'b' then index is 1
        return ord(ch) - ord('a')

    def insert(self, word):
        node = self.root
        # loop through all the chars in the word
        for char in word:
            # get the index where the node for the char should be
            index = self.charToIndex(char)
            # if the node does not exist, create it
            if not node.children[index]:
                node.children[index] = TrieNode()
            # move to the next node
            node = node.children[index]
        # mark the last node as the end of the word
        node.isEndOfWord = True
```

### Complexity

**Time Complexity**: `O(n)` - Where n is the length of the word. This is when the word doesn't share any prefix with the words already in the Trie or is longer than any word in the Trie.

**Space Complexity**:

- *Best Case*: `O(1)` - When the word is entirely a prefix of an existing word or shares a complete prefix with words in the Trie.
 - *Worst Case*: `O(n)` - When the word doesn't share any characters with the words in the Trie.

## Searching in Trie Data Structure

