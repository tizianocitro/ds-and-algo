# Stack

A stack is a linear data structure that follows a particular order of operation. This order can either be **Last In First Out (LIFO)** or **First In Last Out (FILO)**.

Imagine you have a pile of books that you plan to read. You keep adding books to the top of the pile. When you're ready to start reading, you take a book from the top of the pile. The last book you added to the pile is the first one you read. That's LIFO - the principle that stack data structures operate on.

What makes stacks so unique is their simplicity. Despite being straightforward, they can be incredibly powerful when used in the right way.

## Real-world Examples of Stacks

Before diving into technicalities, let's familiarize ourselves with stacks in our daily lives. Stacks are everywhere around us, even if we might not notice them. Here are some examples to help you relate:

1. **Stack of Books**: This is perhaps the simplest example. A pile of books is a stack. The book on the top was the last one added and will be the first one removed.
2. **Stack of Plates**: Picture a stack of plates at a buffet. The first plate you'll take is the one on top, which was the last one put on the stack.
3. **Web Browser History**: Every time you visit a new webpage, it's added to the top of your history stack. When you hit the back button, you're "popping" pages off the top of the stack.
4. **Undo Function in Software Applications**: The undo function in software applications uses a stack to remember actions. The most recent action is on top and will be the first one undone.

Looking at these examples, it's clear that stacks are not just a theoretical concept but a practical one that we use unconsciously in our daily lives.

## The LIFO Principle

As mentioned earlier, stacks in data structures operate on the Last-In, First-Out (LIFO) principle. This means that the last item added to the stack is the first one that gets taken out.

As mentioned earlier, stacks in data structures operate on the Last-In, First-Out (LIFO) principle. This means that the last item added to the stack is the first one that gets taken out.

There are four key operations that you can perform on a stack:

1. **Push**: This is how we add an element to the stack. The element is always added to the top.
2. **Pop**: This is the removal of an element from the stack. The element removed is always from the top.
3. **Peek or Top**: This operation allows us to see the element on the top of the stack without removing it.
4. **IsEmpty**: This operation checks if the stack is empty.

## Operations on Stack

This section aims to describe the main operations involved in manipulating a stack: push, pop, peek, and isEmpty. We will examine these operations closely, detailing their functionality, providing coding examples, and highlighting their importance in problem-solving.

Stack operations and their time complexities:

![Stack operations and their time complexities](https://github.com/tizianocitro/ds-and-algo/blob/main/assets/stack_operations.png "Stack operations and their time complexities")

### Push Operation

The `push` operation adds a new element to the top of the stack. Think of it like placing a new dish on top of a pile in your sink - the new dish (our data) is added to the top of the pile (our stack).

In programming, the push operation usually involves a few steps. First, we check if there's room to add a new element (we'll discuss this in more detail when we talk about stack overflow). If there's room, we add the new element to the top of the stack.

### Pop Operation

The `pop` operation removes the stack's topmost element. It's like removing the top dish from our pile in the sink.

In code, popping an element from a stack is usually done in two parts. First, we check if there are any elements to remove (we'll look at this more when we discuss stack underflow). If there are elements, we remove the top one.

### Peek or Top Operation

The `peek` or `top` operation allows us to look at the top element of the stack without removing it. It's like looking at the top dish in our sink pile without touching it.

This operation can be handy when you need to know what's on top of your stack, but you don't want to change anything. It's a read-only operation.

### IsEmpty Operation
The `isEmpty` operation checks if the stack is empty. This operation is essential for preventing errors when popping an element from an empty stack (known as stack underflow).

An empty stack will return `true` when the `isEmpty` operation is performed, while a stack with one or more elements will return `false`.

### Putting it All Together
Here's a brief coding example to show how these operations can be used together.

```python
class Stack:
    def __init__(self):
        # initialize an empty list to represent the stack
        self.stack = []

    def isEmpty(self):
        # check if the stack is empty by comparing it to an empty list
        return self.stack == []

    def push(self, data):
        # add the given data to the top of the stack (end of the list)
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            # if the stack is empty, return a message indicating so
            return 'Stack is empty'
        # remove and return the top element from the stack (last item in the list), using array's pop method
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            # if the stack is empty, return a message indicating so
            return 'Stack is empty'
        # return the top element from the stack without removing it
        return self.stack[-1]
```

## Dealing with Stack Overflow and Underflow
Stack overflow and underflow are two situations you might encounter when working with stacks. A stack overflow occurs when you try to push an element onto a stack that's already full, while stack underflow occurs when you try to pop an element from an empty stack.

Handling these situations properly is crucial to preventing runtime errors and ensuring that your code runs smoothly. Depending on the programming language and the specific implementation of the stack, you might have different ways of handling these situations. It's always a good idea to check for stack overflow and underflow before performing push and pop operations.

## Implementing Stack Data Structure

In this section, we'll cover how to implement a stack data structure using different data structures: array and linked list.

### Stack Implementation Using an Array

Implementing a stack using an array is one of the most straightforward ways.

```python
class Stack:
    def __init__(self, size):
        # initialize the stack with a specified size
        self.stack = [None] * size
        # initialize the top pointer to -1, indicating an empty stack
        self.top = -1

    def push(self, data):
        # check if the stack is full
        if self.top == len(self.stack) - 1:
            raise Exception('Stack is full')
        # increment the top pointer
        self.top += 1
        # add the data to the stack at the current top position
        self.stack[self.top] = data

    def pop(self):
        # check if the stack is empty
        if self.isEmpty():
            raise Exception('Stack is empty')
        # retrieve the data from the top of the stack
        data = self.stack[self.top]
        # remove the data from the stack by setting it to None
        self.stack[self.top] = None
        # decrement the top pointer to point to the new top of the stack
        self.top -= 1
        # return the popped data
        return data

    def peek(self):
        # check if the stack is empty
        if self.isEmpty():
            raise Exception('Stack is empty')
        # return the data at the top of the stack without removing it
        return self.stack[self.top]

    def isEmpty(self):
        # check if the stack is empty by examining the top pointer
        return self.top == -1
```

The primary advantage of using an array for implementing a stack is that it's simple and requires no additional setup. However, the size of the array can limit the stack size, leading to a stack overflow.

### Stack Implementation Using Linked List

An alternative way of implementing a stack is by using a linked list. This method can overcome the size limitation issue present in the array implementation.

```python
class Stack:
    class Node:
        def __init__(self, data):
            # store the data in this node
            self.data = data
            # initialize the next node as None
            self.next = None

    def __init__(self):
        # initialize the top of the stack as None
        self.top = None

    def pop(self):
        if self.isEmpty():
            # raise exception if the stack is empty
            raise IndexError("pop from empty stack")
        # store the top item's data
        item = self.top.data
        # update the top to be the next node
        self.top = self.top.next
        # return the popped item
        return item

    def push(self, item):
        # create a new node with the provided data
        t = self.Node(item)
        # set the next of this new node to be the current top
        t.next = self.top
        # update the top to be the new node
        self.top = t

    def peek(self):
        if self.isEmpty():
            # raise exception if the stack is empty
            raise IndexError("peek from empty stack")
        # return the top item's data
        return self.top.data

    def isEmpty(self):
        # return True if the stack is empty, False otherwise
        return self.top is None
```

The key difference here is that we're using a Node class to create nodes and link them together to form a stack. This method allows our stack to be dynamically sized, avoiding the overflow issue we saw with arrays.

### Stack Implementation in DIfferent Languages

Here is how different programming languages implement the stack class:

| Language | API |
| --------- | ------- |
| Python | Implemented through List |
| JavaScript | Implemented through Array |
| Java | java.util.Stack |
| C++ | std::stack |

## Applications of Stack

With a solid understanding of stack operations and their implementation, it's time to bring it all together by exploring the real-world applications of stacks. This data structure has a multitude of uses across many different areas in computer science, from memory management and compiler design to problem-solving in data analysis.

### Memory Management

One of the primary uses of stacks is in memory management. Ever wondered how your computer remembers which functions it's running and in which order? The answer is stacks! When a function is called in a program, the system 'pushes' it onto a call stack. When the function finishes running, it's 'popped' off the stack. This mechanism allows for nested function calls, where one function can call another.

This is also how recursion works in programming. When a function calls itself, each recursive call is added to the stack with its own set of variables. Once the base case is met, the functions start resolving and are popped off the stack one by one.

### Expression Evaluation and Syntax Parsing

Another critical application of stacks is in evaluating mathematical expressions and parsing syntax in code compilers. Consider an arithmetic expression like `2 + 3 * 4`. Before performing the operations, we need to check the precedence of the operators to get the correct result. Here, stacks come in handy to apply the **BODMAS rule (Bracket, Order, Division and Multiplication, Addition and Subtraction)**.

Storing operators in a stack can help manage their execution order. Similar logic applies when compilers parse code syntax. They use stacks to check if all opening brackets have matching closing ones, which helps validate the syntax.

### Undo Mechanism in Software Applications

Each action you perform is pushed onto a stack. When you hit 'undo', the most recent action is popped from the stack and reversed. It's a practical and elegant solution to a problem we encounter every day.

### Backtracking Algorithms

Backtracking algorithms solve problems by trying out solutions and undoing them if they don't lead to a solution. This is common in puzzles like Sudoku, the Eight Queens problem, and the Knight's Tour problem.

In such scenarios, stacks are used to store the intermediate stages of the problem. When an attempted solution doesn't work out, the algorithm can 'pop' back to a previous state and try a different path. It's like having a 'save game' feature when you're tackling a challenging puzzle.

### Depth-First Search (DFS)

Stacks are also used in graph algorithms, specifically **Depth-First Search (DFS)**. DFS explores a graph by visiting a node and recursively investigating all its unvisited neighbors. The algorithm uses a stack to remember which nodes to visit next when it finishes exploring a path.

By 'pushing' unvisited nodes onto the stack and 'popping' them once visited, DFS systematically explores every node in the graph. This method is particularly useful in network routing, AI behavior in games, and detecting cycles in a graph.

### Web Page History in Browsers

An everyday example of stacks in action is web page history in a browser. When you click a link, your current page is 'pushed' onto a stack, and you're taken to a new page. If you hit the 'back' button, your browser 'pops' the topmost page off the stack, taking you back to where you were. It's a simple, intuitive way to navigate the vast expanse of the internet.
