# 0/1 Knapsack Pattern

0/1 Knapsack pattern is based on the famous problem with the same name which is efficiently solved using **Dynamic Programming (DP)**.

In this pattern, there is a set of problems that helps in developing an understanding of DP. By firstly solving them with a brute-force recursive solution, it is possible to see the overlapping subproblems, i.e., realizing that we are solving the same problems repeatedly. After the recursive solution, we will modify the algorithm to apply advanced techniques of **Memoization** and **Bottom-Up Dynamic Programming** to develop a complete understanding of this pattern.

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

### Time and Space Complexity

The above algorithm’s time complexity is exponential `O(2^n)`, where `n` represents the total number of items. This can also be confirmed from the above recursion tree. As we can see, we will have a total of `31` recursive calls – calculated through `(2^n) + (2^n) - 1`, which is asymptotically equivalent to `O(2^n)`.

The space complexity is `O(n)`. This space will be used to store the recursion stack. Since the recursive algorithm works in a `depth-first fashion`, which means that we can’t have more than `n` recursive calls on the call stack at any time.