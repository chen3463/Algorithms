/*

Description
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

For n=0, we think the answer is 1.

Example
Example 1:

Input: 3
Output: 4
Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
Example 2:

Input: 4
Output: 7
Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.

*/

class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n == 0:
            return 1

        DP = [0 for _ in range(n)]

        if n == 1:
            return 1

        if n == 2:
            return 2

        if n == 3:
            return 4

        DP[0] = 1
        DP[1] = 2
        DP[2] = 4
        for i in range(3, n):
            DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]

        return DP[n - 1]
            
