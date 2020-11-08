
'''
Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example
Example 1:
	Input:  [[5]],2
	Output: false
	
	Explanation: 
	false if not included.
	
Example 2:
	Input:  [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
],3
	Output: true
	
	Explanation: 
	return true if included.
Challenge
O(log(n) + log(m)) time
'''


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix[0]), len(matrix)
        left, right = 0, m * n - 1 
        
        while left + 1 < right:
            mid = (right + left) // 2 
            value = self.get(matrix, mid)
            if value > target:
                right = mid
                
            else:
                left = mid
                
        if self.get(matrix, left) == target:
            return True
            
        if self.get(matrix, right) == target:
            return True
            
        return False
        
    def get(self, matrix, index):
        x = index // len(matrix[0])
        y = index % len(matrix[0])
        return matrix[x][y]
