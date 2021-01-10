/*

A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Example
Example 1:

Input: n = 1, m = 3
Output: 1	
Explanation: Only one path to target position.
Example 2:

Input:  n = 3, m = 3
Output: 6	
Explanation:
	D : Down
	R : Right
	1) DDRR
	2) DRDR
	3) DRRD
	4) RRDD
	5) RDRD
	6) RDDR
Notice
m and n will be at most 100.
The answer is guaranteed to be in the range of 32-bit integers
*/

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            matrix[i][0] = 1
            
        for j in range(n):
            matrix[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
                
        return matrix[m - 1][n - 1]
