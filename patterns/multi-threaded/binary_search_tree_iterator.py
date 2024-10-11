# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/binary-search-tree-iterator-medium

'''Problem:
Implement an iterator for the in-order traversal of a binary search tree (BST). That is, given a BST, we need to implement two functions:
- bool hasNext(): Returns true if at least one element is left in the in-order traversal of the BST.
- int next(): Return the next element in the in-order traversal of the BST.

Given the in-order traversal of a tree: [1, 4, 10, 14, 15, 19, 20]
This is the expected output from the algorithm based on different calls:
    hasNext() -> true
    next() -> 1
    next() -> 4
    hasNext() -> true
    next() -> 10
    next() -> 14
    next() -> 15
    next() -> 19
    next() -> 20
    hasNext() -> false
'''

'''Solution:
Solution two algorithm does not have thread-safety. The algorithm would fail if multiple threads access the same BSTIterator object.
We could get a synchronization issue in the next() function for the following two lines:
    TreeNode tmpNode = stack.pop();
    traverseLeft(tmpNode.right);
If two threads access the function concurrently, the stack could end up in a bad state.
Suppose one thread executes the first line to pop an element from the stack. Before it executes the next line (to traverse the left subtree),
another thread which is also processing these lines, can also pop another element from the stack, thus, making the stack invalid.
This means we need to synchronize this function so that only one thread is allowed to process next() at any time.

Then, we can make next() multi-threaded so that can return the element to the caller immediately and spawn a separate thread to perform
the post-processing required to traverse the left subtree. In the next() function, we do have the required node available right away, but we could
not return to the caller before we traverse the left subtree of the right child of the current node:
    traverseLeft(tmpNode.right);
we can spawn a new thread to process this traversal and return the element to the caller. This way, the caller is unblocked as it has the data quickly,
and all the post-processing is done in a separate thread. This makes the algorithm a bit complex though. Now, whenever we are starting a new execution
of next() or hasNext(), we need to ensure any previous thread doing the post-processing has finished. This means that we have to add a check before
processing next() or hasNext() to wait and call join() on the previous thread if it has not already finished.
'''

# solution one multi-threaded version of solution two
# Complexity:
# O(v) time - where v is the number of nodes in the binary tree
# O(h) space - for the array that stores the in-order traversal of the tree where h is the height of the tree
# and h = v in the worst case scenario, where the tree is like a linked list
import multiprocessing

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root):
        self.stack = multiprocessing.Manager().list()
        self.lock = multiprocessing.Lock()
        self.process = None
        self._traverseLeft(self.stack, root)

    # returns whether we have a next smallest number
    def hasNext(self):
        self._checkAndJoinProcess()
        # if we have elements in the stack, then we have a next number
        return self.stack

    # returns the next smallest number
    def next(self):
        self.lock.acquire()
        self._checkAndJoinProcess()
        node = self.stack.pop()

        # spawn a new process to traverse the left sub-tree of the right child of the current node
        self.process = multiprocessing.Process(target=self._traverseLeft, args=(self.stack, node.right))
        self.process.start()

        # it is possible to use a thread instead of a process
        # import threading
        # self.thread = threading.Thread(target=self._traverseLeft, args=(self.stack, node.right))
        # self.thread.start()

        self.lock.release()
        return node.val

    # traverse the left sub-tree to push all nodes on the stack
    def _traverseLeft(self, stack, node):
        while node is not None:
            stack.append(node)
            node = node.left

    def _checkAndJoinProcess(self):
        if self.process and self.process.is_alive():
            self.process.join()

'''Solution:
We know that we can perform the in-order traversal of a BST recursively. But for the iterator, we can’t use recursion as we can’t stop recursion
in the middle to return the required element; this way, we will lose the recursive state of the traversal. Also, we didn’t want to perform the
in-order traversal every time next() or hasNext() is called; this will make these function O(v) operations.

We can transform a recursive solution to make it iterative using a stack. This way, we can control the recursion by saving the state of the
in-order traversal of the BST in the stack, and later we can resume the tree traversal when next() is called again.
'''

# solution two
# Complexity:
# O(v) time - where v is the number of nodes in the binary tree
# O(h) space - for the array that stores the in-order traversal of the tree where h is the height of the tree
# and h = v in the worst case scenario, where the tree is like a linked list
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root):
        self.stack = list()
        self._traverseLeft(root)

    # returns whether we have a next smallest number
    def hasNext(self):
        # if we have elements in the stack, then we have a next number
        return self.stack

    # returns the next smallest number
    def next(self):
        node = self.stack.pop()
        self._traverseLeft(node.right)
        return node.val

    # traverse the left sub-tree to push all nodes on the stack
    def _traverseLeft(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

# solution three
# Complexity:
# O(v) time - where v is the number of nodes in the binary tree
# O(v) space - for the array that stores the in-order traversal of the tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root):
        self.arr = []
        self.ix = 0
        self._inorder(root)

    # returns whether we have a next smallest number
    def hasNext(self):
        return self.ix < len(self.arr)

    # returns the next smallest number
    def next(self):
        node = self.arr[self.ix]
        self.ix += 1
        return node

    def _inorder(self, node):
        if node is None:
            return

        self._inorder(node.left)
        self.arr.append(node.val)
        self._inorder(node.right)

