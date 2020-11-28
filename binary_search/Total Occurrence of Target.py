'''
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

Example
Example1:

Input: [1, 3, 3, 4, 5] and target = 3, 
Output: 2.
Example2:

Input: [2, 2, 3, 4, 6] and target = 4, 
Output: 1.
Example3:

Input: [1, 2, 3, 4, 5] and target = 6, 
Output: 0.
Challenge
Time complexity in O(logn)
'''

class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0
           
        most_left = self.find_most_left(A, 0, len(A) - 1, target)
        most_right = self.find_most_right(A, 0, len(A) - 1, target)
        if most_left == -1 or most_right == -1:
            return 0
            
        return most_right - most_left + 1 
        
    def find_most_left(self, A, left, right, target):    
        while left + 1 < right:
            mid = (left + right) // 2 
            if target <= A[mid]:
                right = mid
            else:
                left = mid
            
        if A[left] == target:
            return left
        
        if A[right] == target:
            return right
        
        return -1
            
    def find_most_right(self, A, left, right, target):    
        while left + 1 < right:
            mid = (left + right) // 2 
            if target >= A[mid]:
                left = mid
            else:
                right = mid
            
        if A[right] == target:
            return right
        
        if A[left] == target:
            return left 
            
        return -1
