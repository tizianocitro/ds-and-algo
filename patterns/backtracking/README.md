# Backtracking

Backtracking is an algorithmic technique that uses the **brute-force approach** to solve a problem.

> Brute-force approach states that for any problem, we should try out all possible solutions and pick up those solutions that satisfy the problem constraints.

In backtracking, we build a solution incrementally and follow the approach that if the current solution can’t lead to a valid solution, abandon it and backtrack (or go back) to try another solution. Because of this, **recursion** becomes a suitable technique for solving backtracking problems.

*Dynamic Programming (DP)* uses a similar approach where we try out all possible solutions (using *Memoization*) to pick up the most optimized solution. **DP is used to solve optimization problems**; **backtracking**, on the other hand, **is mostly used when multiple valid solutions are possible for a problem**.

## Example

Imagine we want to plant, in a straight line, three fruit trees `Apple`, `Orange`, and `Mango`. What are the possible ways these trees can be planted? The only restriction we have is that *`Apple` and `Orange` trees can’t be placed next to each other*.

Following a brute-force approach, we can find all possible combinations in which the three trees can be placed and pick those that fulfill the given constraint.

Let’s try finding all the possible arrangements.

The first tree can be of any kind, `Apple`, `Orange`, or `Mango`. If our first tree is `Apple`, the second tree can be `Orange` or `Mango`. If we place `Orange` as our second tree, then our constraint is not fulfilled (which was not to place `Apple` and `Orange` together). Hence it is not a valid arrangement; therefore, we go back (i.e., backtrack) and place `Mango` as our second tree. Now, we can place `Orange` in the third place; this arrangement fulfills the problem constraint.

The following diagram shows all possible arrangements:

![All possible arrangements](/assets/backtracking.png "All possible arrangements")

From the above diagram, we can clearly see that the two valid arrangements are: `[Apple, Mango, Orange]` and `[Orange, Mango, Apple]`.

This approach of evaluating all possible solutions, going back whenever we see that a certain constraint can’t be met, and trying out other possible solutions is called **backtracking**.