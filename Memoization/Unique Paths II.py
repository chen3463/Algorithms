'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example
Example 1:
	Input: [[0]]
	Output: 1


Example 2:
	Input:  [[0,0,0],[0,1,0],[0,0,0]]
	Output: 2
	
	Explanation:
	Only 2 different path.
	

'''


class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        matrix = [[0] * m for _ in range(n)]
        
        for i in range(m):
            if obstacleGrid[0][i] == 0:
                matrix[0][i] = 1
            else:
                break
            
        for j in range(n):
            if obstacleGrid[j][0] == 0:
                matrix[j][0] = 1
            else:
                break
        print(matrix)
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
                    
        return matrix[n - 1][m - 1]
