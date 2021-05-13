/*
Description
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.

If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
Example
Example 1:

Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]
Example 2:

Input:
[[0,1,0],[0,0,1],[0,0,0]]
Output:
-1
*/

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        m, n = len(grid), len(grid[0])
        DP = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        DP[0][0] = 0
        for j in range(n):
            for i in range(m):
                for (x, y) in [(-1, -2), (1, -2), (-2, -1), (2, -1)]:
                    x_pre, y_pre = i + x, j + y
                    if grid[i][j] == 0 and 0 <= x_pre < m and 0 <= y_pre < n:
                        DP[i][j] = min(DP[i][j], DP[x_pre][y_pre] + 1)

        if DP[m - 1][n - 1] < sys.maxsize:
            return DP[m - 1][n - 1]

        return -1
