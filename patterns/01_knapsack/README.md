# 0/1 Knapsack Pattern

0/1 Knapsack pattern is based on the famous problem with the same name which is efficiently solved using **Dynamic Programming (DP)**.

In this pattern, there is a set of problems that helps in developing an understanding of DP. By firstly solving them with a brute-force recursive solution, it is possible to see the overlapping subproblems, i.e., realizing that we are solving the same problems repeatedly. After the recursive solution, we will modify the algorithm to apply advanced techniques of **Memoization** and **Bottom-Up Dynamic Programming** to develop a complete understanding of this pattern.

## What is Dynamic Programming?

**Dynamic Programming (DP)** is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

Let's take the example of the **Fibonacci numbers**. As we all know, Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers. The first few Fibonacci numbers are `0, 1, 1, 2, 3, 5, and 8`, and they continue on from there.

If we are asked to calculate the **nth Fibonacci number**, we can do that with the following equation:

```python
Fib(n) = Fib(n - 1) + Fib(n - 2), for n > 1
```

As we can clearly see here, to solve the overall problem (i.e. `Fib(n)`), we broke it down into two smaller subproblems (which are `Fib(n-1)` and `Fib(n-2)`). This shows that we can use DP to solve this problem.

### Characteristics of Dynamic Programming

Before moving on to understand different methods of solving a DP problem, let’s first take a look at **what are the characteristics of a problem that tells us that we can apply DP to solve it**.

#### Overlapping Subproblems

Subproblems are smaller versions of the original problem. **Any problem has overlapping sub-problems if finding its solution involves solving the same subproblem multiple times**. Take the example of the Fibonacci numbers; to find the `Fib(4)`, we need to break it down into the following sub-problems:

![Visual representation of Fib(4)](/assets/fib_dp.png "Visual representation of Fib(4)")

We can clearly see the overlapping subproblem pattern here, as `fib(2)` has been evaluated **twice** and `fib(1)` has been evaluated **three times**.

#### Optimal Substructure Property

**Any problem has optimal substructure property if its overall optimal solution can be constructed from the optimal solutions of its subproblems**. For Fibonacci numbers, as we know:

```python
Fib(n) = Fib(n - 1) + Fib(n - 2)
```

This clearly shows that a problem of size `n` has been reduced to subproblems of size `n - 1` and `n - 2`. Therefore, Fibonacci numbers have optimal substructure property.

### Approaches

#### Top-down with Memoization

In this approach, we try to solve the bigger problem by recursively finding the solution to smaller sub-problems. Whenever we solve a sub-problem, we cache its result so that we don’t end up solving it repeatedly if it’s called multiple times. Instead, we can just return the saved result. This technique of storing the results of already solved subproblems is called **Memoization**.

We’ll see this technique in our example of Fibonacci numbers. First, let's see the non-DP recursive solution for finding the `nth Fibonacci number`:

```python
class Solution:
  def calculateFibonacci(self, n):
    if n < 2:
      return n

    return self.calculateFibonacci(n - 1) + self.calculateFibonacci(n - 2)
```

As we saw above, this problem shows the overlapping subproblems pattern, so let's make use of memoization here. We can use an array to store the already solved subproblems:

```python
class Solution:
  def calculateFibonacci(self, n):
    # memoization cache
    memo = [-1 for x in range(n+1)]

    return self.calculateFibonacciRecur(memo, n)

  def calculateFibonacciRecur(self, memo, n):
    if n < 2:
      return n

    # if we have already solved this subproblem,
    # simply return the result from the memoization cache
    if memo[n] != -1:
      return memo[n]

    memo[n] = self.calculateFibonacciRecur(
      memo, n - 1) + self.calculateFibonacciRecur(memo, n - 2)

    return memo[n]

```

#### Bottom-up with Tabulation

Tabulation is the opposite of the top-down approach and avoids recursion. In this approach, we solve the problem "bottom-up" (i.e. by solving all the related sub-problems first). This is typically done by filling up an `n-dimensional table`. Based on the results in the table, the solution to the top/original problem is then computed.

Tabulation is the opposite of Memoization, as in Memoization we solve the problem and maintain a map of already solved sub-problems. In other words, in memoization, we do it top-down in the sense that we solve the top problem first (which typically recurses down to solve the sub-problems).

Let's apply Tabulation to our example of Fibonacci numbers. Since we know that every Fibonacci number is the sum of the two preceding numbers, we can use this fact to populate our table.

Here is the code for our bottom-up dynamic programming approach:

```python
class Solution:
  def calculateFibonacci(self, n):
    # our table
    dp = [0, 1]

    for i in range(2, n + 1):
      # fill the table as we solve the subproblems
      dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]
```

## 0/1 Knapsack

Given the weights and profits of `N` items, we are asked to put these items in a knapsack with a capacity `C`. The goal is to get the maximum profit out of the knapsack items. Each item can only be selected once, as we don’t have multiple quantities of any item.

### Example

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

- Items: {Apple, Orange, Banana, Melon}
- Weights: {2, 3, 1, 4}
- Profits: {4, 5, 3, 7}
- Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than `5`:

1. Apple + Orange (total weight 5) => 9 profit
2. Apple + Banana (total weight 3) => 7 profit
3. Orange + Banana (total weight 4) => 8 profit
4. Banana + Melon (total weight 5) => 10 profit

This shows that `Banana + Melon` is the best combination as it gives us the maximum profit, and the total weight does not exceed the capacity.

## Brute-force Solution

A basic brute-force solution could be to try all combinations of the given items (as we did above), allowing us to choose the one with maximum profit and a weight that doesn’t exceed `C`. Take the example of four items (`A, B, C, and D`), as shown in the diagram below. To try all the combinations, our algorithm will look like:

```python
for each item 'i' 
  create a new set which INCLUDES item 'i' if the total weight does not exceed the capacity, and recursively process the remaining capacity and items

  create a new set WITHOUT item 'i', and recursively process the remaining items

return the set from the above two sets with higher profit
```

Here is a visual representation of our algorithm:

![Visual representation of the algorithm](/assets/01_knapsack_pattern.png "Visual representation of the algorithm")

All `green boxes` have a total weight that is less than or equal to the capacity `7`, and all the `red ones` have a weight that is more than `7`. The best solution we have is with items `[B, D]` having a total profit of `22` and a total weight of `7`.

### Code

```python
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        return self.knapsack_recursive(profits, weights, capacity, 0)

    def knapsack_recursive(self, profits, weights, capacity, current_index):
        # base checks
        if capacity <= 0 or current_index >= len(profits):
            return 0

        # recursive call after choosing the element at the current_index
        # if the weight of the element at current_index exceeds the capacity,
        # we shouldn't process this
        profit1 = 0
        if weights[current_index] <= capacity:
            profit1 = profits[current_index] + self.knapsack_recursive(
                profits, weights, capacity - weights[current_index], current_index + 1)

        # recursive call after excluding the element at the current_index
        profit2 = self.knapsack_recursive(profits, weights, capacity, current_index + 1)

        return max(profit1, profit2)
```

### Time and Space Complexity

The above algorithm’s time complexity is exponential `O(2^n)`, where `n` represents the total number of items. This can also be confirmed from the above recursion tree. As we can see, we will have a total of `31` recursive calls – calculated through `(2^n) + (2^n) - 1`, which is asymptotically equivalent to `O(2^n)`.

The space complexity is `O(n)`. This space will be used to store the recursion stack. Since the recursive algorithm works in a `depth-first fashion`, which means that we can’t have more than `n` recursive calls on the call stack at any time.

## Overlapping Sub-problems

Let’s visually draw the recursive calls of the previous brute-force solution to see if there are any overlapping sub-problems. As we can see, in each recursive call, profits and weights arrays remain constant, and only `capacity` and `current_index` change. For simplicity, let’s denote `capacity` with `c` and `current_index` with `i`:

![Visual representation of overlapping sub-problems in the algorithm](/assets/01_knapsack_pattern_overlapping.png "Visual representation of overlapping sub-problems in the algorithm")

We can clearly see that `c:4, i=3` has been called twice. Hence we have an overlapping sub-problems pattern. We can use `Memoization` to solve overlapping sub-problems efficiently.

## Top-down Dynamic Programming with Memoization

`Memoization` is when we store the results of all the previously solved sub-problems and return the results from memory if we encounter a problem that has already been solved.

Since we have two changing values (`capacity` and `current_index`) in our recursive function `knapsackRecursive()`, we can use a two-dimensional array to store the results of all the solved sub-problems. As mentioned above, we need to store results for every sub-array (i.e., for every possible index `i`) and every possible capacity `c`.

### Code

```python
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # create a two dimensional array for Memoization,
        # each element is initialized to '-1'
        dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]

        return self.knapsack_recursive(dp, profits, weights, capacity, 0)

    def knapsack_recursive(self, dp, profits, weights, capacity, current_index):
        # base checks
        if capacity <= 0 or current_index >= len(profits):
            return 0

        # if we have already solved a similar problem, return the result from memory
        if dp[current_index][capacity] != -1:
            return dp[current_index][capacity]

        # recursive call after choosing the element at the current_index
        # if the weight of the element at current_index exceeds the capacity, we
        # shouldn't process this
        profit1 = 0
        if weights[current_index] <= capacity:
            profit1 = profits[current_index] + self.knapsack_recursive(
                dp, profits, weights, capacity - weights[current_index], current_index + 1)

        # recursive call after excluding the element at the current_index
        profit2 = self.knapsack_recursive(
            dp, profits, weights, capacity, current_index + 1)

        # add the problem to the solved ones
        dp[current_index][capacity] = max(profit1, profit2)

        return dp[current_index][capacity]
```

### Time and Space Complexity

Since our memoization array `dp[profits.length][capacity + 1]` stores the results for all subproblems, we can conclude that we will not have more than `nc` subproblems (where `n` is the number of items and `c` is the knapsack capacity). This means that our time complexity will be `O(nc)`.

The above algorithm will use `O(nc)` space for the memoization array. Other than that, we will use `O(n)` space for the recursion call-stack. So the total space complexity will be `O(nc + n)`, which is asymptotically equivalent to `O(nc)`.

### How can we find the selected items?

Here's the modified code to get the selected items:

```python
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # create a two dimensional array for Memoization, each element
        # is initialized to '-1' and [] to keep track also of the items
        dp = [[(-1, []) for x in range(capacity + 1)] for y in range(len(profits))]

        return self.knapsack_recursive(dp, profits, weights, capacity, 0)

    def knapsack_recursive(self, dp, profits, weights, capacity, current_index):
        # base checks
        if capacity <= 0 or current_index >= len(profits):
            return 0, []

        # if we have already solved a similar problem, return the result from memory,
        # it happens if the profit is not set to '-1' in dp
        if dp[current_index][capacity][0] != -1:
            return dp[current_index][capacity]

        # recursive call after choosing the element at the current_index
        # if the weight of the element at current_index exceeds the capacity, we
        # shouldn't process this
        profit1, items1 = 0, []
        if weights[current_index] <= capacity:
            profit1, items1 = self.knapsack_recursive(
                dp, profits, weights, capacity - weights[current_index], current_index + 1)
            profit1 += profits[current_index]
            items1 += [current_index]

        # recursive call after excluding the element at the current_index
        profit2, items2 = self.knapsack_recursive(
            dp, profits, weights, capacity, current_index + 1)

        # add the problem to the solved ones
        if profit1 > profit2:
            dp[current_index][capacity] = (profit1, items1)
        else:
            dp[current_index][capacity] = (profit2, items2)

        return dp[current_index][capacity]
```

## Bottom-up Dynamic Programming

Let’s try to populate our `dp[][]` array from the above solution by working in a `bottom-up fashion`. Essentially, we want to find the maximum profit for every sub-array and every possible capacity. This means that `dp[i][c]` will represent the maximum knapsack profit for capacity `c` calculated from the first `i` items.

So, for each item at index `i (0 <= i < items.length)` and capacity `c (0 <= c <= capacity)`, we have two options:

1. **Exclude the item at index `i`**. In this case, we will take whatever profit we get from the sub-array excluding this item => `dp[i - 1][c]`.
2. **Include the item at index `i` if its weight is not more than the `capacity`**. In this case, we include its profit plus whatever profit we get from the remaining capacity and from remaining items => `profit[i] + dp[i - 1][c - weight[i]]`.

Finally, our optimal solution will be maximum of the above two values: `dp[i][c] = max(dp[i-1][c], profit[i] + dp[i - 1][c - weight[i]])`.

### Code

```python
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [[0 for x in range(capacity+1)] for y in range(n)]

        # populate the capacity = 0 columns, with '0' capacity we have '0' profit
        for i in range(0, n):
            dp[i][0] = 0

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, capacity + 1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[i - 1][c - weights[i]]
                # exclude the item
                profit2 = dp[i - 1][c]
                # take maximum
                dp[i][c] = max(profit1, profit2)

        # maximum profit will be at the bottom-right corner.
        return dp[n - 1][capacity]
```

### Time and Space complexity

The above solution has the time and space complexity of `O(nc)`, where `n` represents total items, and `c` is the maximum capacity.

### How can we find the selected items?

As we know, the final profit is at the **bottom-right corner**. Therefore, we will start from there to find the items that will be going into the knapsack.

As you remember, at every step, we had two options: include an item or skip it. If we skip an item, we take the profit from the remaining items (i.e., from the cell right above it); if we include the item, then we jump to the remaining profit to find more items.

Let’s understand this from the above example:

![Selected items](/assets/01_knapsack_pattern_find_items.png "Selected items")

1. `22` did not come from the top cell (which is `17`); hence we must include the item at index `3` (which is item `D`).
2. Subtract the profit of item `D` from `22` to get the remaining profit `6`. We then jump to profit `6` on the same row.
3. `6` came from the top cell, so we jump to row `2`.
4. Again, `6` came from the top cell, so we jump to row `1`.
5. `6` is different from the top cell, so we must include this item (which is item `B`).
6. Subtract the profit of `B` from `6` to get profit `0`. We then jump to profit `0` on the same row. As soon as we hit zero remaining profit, we can finish our item search.
7. Thus, the items going into the knapsack are `{B, D}`.

### Code With Selected Items

```python
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [[0 for x in range(capacity + 1)] for y in range(n)]

        # populate the capacity = 0 columns, with '0' capacity we have '0' profit
        for i in range(0, n):
            dp[i][0] = 0

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, capacity + 1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[i - 1][c - weights[i]]
                # exclude the item
                profit2 = dp[i - 1][c]
                # take maximum
                dp[i][c] = max(profit1, profit2)

        self.print_selected_elements(dp, weights, profits, capacity)

        # maximum profit will be at the bottom-right corner
        return dp[n - 1][capacity]

    def print_selected_elements(self, dp, weights, profits, capacity):
        print("Selected weights are: ", end='')
        n = len(weights)
        # start from the bottom-right corner
        total_profit = dp[n - 1][capacity]
        for i in range(n - 1, 0, -1):
            if total_profit != dp[i - 1][capacity]:
                print(str(weights[i]) + " ", end='')
                capacity -= weights[i]
                total_profit -= profits[i]

        if total_profit != 0:
            print(str(weights[0]) + " ", end='')
        print()
```

## Improvement of Bottom-up DP solution

We can develop an algorithm that has `O(c)` space complexity because **we only need one previous row to find the optimal solution**.

Here's the code for the improved version:

```python
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        # we only need one previous row to find the optimal solution, overall we need '2' rows
        # the above solution is similar to the previous solution, the only difference is that
        # we use `i % 2` instead if `i` and `(i-1) % 2` instead if `i-1`
        dp = [[0 for x in range(capacity + 1)] for y in range(2)]

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = dp[1][c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(0, capacity + 1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
                # exclude the item
                profit2 = dp[(i - 1) % 2][c]
                # take maximum
                dp[i % 2][c] = max(profit1, profit2)

        return dp[(n - 1) % 2][capacity]
```

The solution above is similar to the previous solution; the only difference is that we use `i % 2` instead of `i` and `(i - 1) % 2` instead of `i - 1`. This solution has a space complexity of `O(2c) = O(c)`, where `c` is the knapsack’s maximum capacity.

This space optimization solution can also be implemented using a single array. It is a bit tricky, but *the intuition is to use the same array for the previous and the next iteration*.

Having a closer look, we need two values from the previous iteration: `dp[c]` and `dp[c - weight[i]]`.

Since our inner loop is iterating over `c:0-->capacity`, let’s see how this might affect our two required values:

1. When we access `dp[c]`, it has not been overridden yet for the current iteration, so it should be fine.
2. `dp[c - weight[i]]` might be overridden if `weight[i] > 0`. Therefore we can’t use this value for the current iteration.

To solve the second case, we can change our inner loop to process in the reverse direction: `c:capacity-->0`. This will ensure that whenever we change a value in `dp[]`, we will not need it again in the current iteration.

```python
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [0 for x in range(capacity + 1)]

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(capacity, -1, -1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[c - weights[i]]
                # exclude the item
                profit2 = dp[c]
                # take maximum
                dp[c] = max(profit1, profit2)

        return dp[capacity]
```