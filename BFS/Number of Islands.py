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
        if not grid:
            return 0
            
        n = len(grid)
        m = len(grid[0])
        visited = set()
        islands = 0
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] and (i, j) not in visited:
                    self.BFS(grid, i, j, visited)
                    islands += 1
                visited.add((i, j))
        
        return islands        
                
    def BFS(self, grid, x, y, visited):
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in self.directions:
                x_next = x + delta_x
                y_next = y + delta_y
                if not self.is_valid(grid, x_next, y_next, visited):
                    continue
                queue.append((x_next, y_next))
                visited.add((x_next, y_next))
                
    def is_valid(self, grid, i, j, visited):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return False
        if (i, j) in visited:
            return False
        return grid[i][j]
            
        
