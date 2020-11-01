'''
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.
'''


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        results = [[float('inf')] * n for _ in range(m)]
        results[0][0] = 0
        directions = [
            [-1, -2],
            [1, -2],
            [-2, -1],
            [2, -1]
        ]
        for j in range(n):
            for i in range(m):
                if grid[i][j]:
                    continue
                for delta_x, delta_y in directions:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < m and 0 <= y < n:
                        results[i][j] = min(results[i][j], results[x][y] + 1)
                        print(i, j, x, y, results)
                    
        if results[m - 1][n - 1] == float('inf'):
            return -1
            
        return results[m - 1][n - 1]
