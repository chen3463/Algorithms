'''
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Example 1:

Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
Example 2:

Input:
[
  [1,1]
]
Output:
1
'''

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(i, j, grid, visited)
                    islands += 1
        return islands

    def bfs(self, x, y, grid, visited):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = collections.deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            for (x_delta, y_delta) in directions:
                x_new = x + x_delta
                y_new = y + y_delta
                if not self.isvalid(x_new, y_new, grid, visited):
                    continue
                queue.append((x_new, y_new))
                visited.add((x_new, y_new))

    def isvalid(self, x, y, grid, visited):
        m, n = len(grid), len(grid[0])
        if not (0 <= x < m and 0 <= y < n):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]
            
        
