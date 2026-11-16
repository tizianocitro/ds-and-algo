# !code: 232, !difficulty: easy, !from: https://leetcode.com/problems/implement-queue-using-stacks, https://neetcode.io/problems/implement-queue-using-stacks

'''Problem:
Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x): pushes element x to the back of the queue.
- int pop(): removes the element from the front of the queue and returns it.
- int peek(): returns the element at the front of the queue.
- boolean empty(): returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively.
  You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Follow-up:
Can you implement the queue such that each operation is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

Constraints:
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty
- All the calls to pop and peek are valid

Input:
    ["MyQueue", "push", "push", "peek", "pop", "empty"]
    [[], [1], [2], [], [], []]
Output: [null, null, null, 1, 1, false]
Explanation:
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
'''

# solution one
# Complexity:
# Time:
# - push: O(n) time - where n is the number of elements in the queue
# - pop: O(1) time
# - peek: O(1) time
# - empty: O(1) time
# O(n) space - where n is the number of elements in the queue
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0

# solution two with amortized O(1) time for push, pop and peek operations
# once s2 is empty, we need to move all elements from s1 to s2 which takes O(n) time,
# but this happens only once for every n pop operations, so the amortized time is O(1)
# Complexity:
# Time:
# - push: O(1) time
# - pop: O(1) amortized time
# - peek: O(1) amortized time
# - empty: O(1) time
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # if s2 is empty, we need to move all elements from s1 to s2 to reverse the order
        # (reverse is the popping order of the queue)
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        # if s2 is empty, we need to move all elements from s1 to s2 to reverse the order
        # (reverse is the popping order of the queue)
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0
