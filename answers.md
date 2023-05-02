# CMPS 2200 Assignment 5
## Answers

**Name:**___Zachary Wiel______


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**

The Greedy Algorithm would start by finding the largest base 2 number less than n, this number would be the first coin. Then the algorithm would find the largest base 2 number less than the difference between n and value of the previous coin(s), this number would be the second coin. The algorithm would repeat until the difference between n and the sum of the value of the coins reaches zero. The algorithm is optimal because there will never be repitition of coin values as all coins are in base 2 and at each step the largest possible base 2 value is being removed.


- **1b.**

The Greedy Algorithm would have a work complexity of O(log(n)) as at each step n is being reduced by at least half. The algorithm has  a span complexity of O(log(n)) as each step is dependent on the previous step's result so there the algorithm cannot be parallelized.


- **2a.**

If the denominations available are 1,4,5,7 and n is $9 then the Greedy Algorithm would incorrectly say that the minimum number of coins is 3 being 7, 1, 1 but the correct answer is 2 being 4, 5. The Greedy algorithm is not optimal as the denominations are not uniform and thus do not breakdown consistently.


- **2b.**

We want to find the minimum number of coins needed to make change for a given amount N using a set of coin denominations. The bottom-up approach begins by calculating the minimum number of coins required for an amount of 1 and builds up to the final result for amount N. The algorithm iterates through each denomination and stores solutions to subproblems in a memoization table.

The work complexity of this dynamic programming solution is O(k*N), where k is the number of denominations and N is the target amount. This complexity arises because we need to fill the memoization table with k rows (one for each denomination) and N columns (one for each amount from 0 to N).
The span complexity of the solution is O(k+N). This is because the longest dependency chain in the algorithm comes from iterating through all denominations and all amounts up to N.

- **3.**

In main
