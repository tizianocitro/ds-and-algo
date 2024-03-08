# Monotonic Stack

A Monotonic Stack is a special kind of stack, a common data structure in computer science, which maintains its elements in a specific order. Unlike a traditional stack, where elements are placed on top of one another based on when they arrive, a Monotonic Stack ensures that the elements inside the stack remain in an increasing or decreasing order. This is achieved by enforcing specific push and pop rules, depending on whether we want an increasing or decreasing monotonic stack.

Monotonic Stacks are powerful tools in coding interviews due to their unique capabilities. They are particularly effective when it comes to problems requiring us to find the next smaller or larger element in a sequence, often referred to as Next Greater Element (NGE) or Next Smaller Element (NSE) problems.

## Types of Monotonic Stacks

Monotonic Stacks can be broadly classified into two types:

1. Monotonically Increasing Stack
2. Monotonically Decreasing Stack

### Monotonically Increasing Stack

A Monotonically Increasing Stack is a stack where elements are arranged in an ascending order from the bottom to the top. Here, every new element that's pushed onto the stack is greater than or equal to the element below it. If a new element is smaller, we pop the elements from the top of the stack until we find an element smaller than or equal to the new element, or the stack is empty. This way, the stack always maintains an increasing order.

![Monotonically Increasing Stack example](/assets/monotonically_increasing_stack.png "Monotonically Increasing Stack example")

### Monotonically Decreasing Stack

A Monotonically Decreasing Stack is a stack where elements are arranged in a descending order from the bottom to the top. When a new element arrives, if it's larger than the element on the top, we keep popping the elements from the stack until we find an element that's larger than or equal to the new element, or the stack is empty. This ensures that the stack always maintains a decreasing order.

![Monotonically Decreasing Stack example](/assets/monotonically_decreasing_stack.png "Monotonically Decreasing Stack example")

## Identifying Problems Suitable for Monotonic Stack

Recognizing when to use a Monotonic Stack is a crucial skill. Here are some key aspects to consider.

### Problem Characteristics

Monotonic Stacks are typically useful when dealing with problems that involve analyzing sequences or arrays, especially when you need to find the next or previous larger or smaller element for each element in the array. If you encounter a problem where the solution seems to require some sort of sequential step-by-step comparison, it's likely a good candidate for using a Monotonic Stack.

### Example Scenarios

One classic sign that a Monotonic Stack might be helpful is when the problem description mentions finding the "next greater element" or the "next smaller element" in an array. Problems that involve finding maximum areas, such as in histograms, can also be solved effectively using Monotonic Stacks. Remember, the key is to identify patterns where a sequential step-by-step comparison is necessary.

## Constructing Monotonic Stacks

