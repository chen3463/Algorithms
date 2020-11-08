'''
Search a 2D Matrix II
中文English
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.
Example
Example 1:

Input:
	[[3,4]]
	target=3
Output:1
Example 2:

Input:
    [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 3
Output:2
Challenge
O(m+n) time and O(1) extra space
'''

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return 0 
        m, n = len(matrix), len(matrix[0])    
        x, y = m - 1, 0
        count = 0
        while x >= 0 and y < n:
            if matrix[x][y] == target:
                count += 1 
                x -= 1 
                y += 1 
            
            elif matrix[x][y] > target:
                x -= 1 
                
            else:
                y += 1 
        
        return count
