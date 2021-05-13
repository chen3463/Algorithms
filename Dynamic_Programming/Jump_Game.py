'''
Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example

Example 1

Input : [2,3,1,1,4]
Output : true
Example 2

Input : [3,2,1,0,4]
Output : false
'''


class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False 
            
        n = len(A)
        
        DP = [False] * n 
        DP[0] = True
        
        for i in range(1, n):
            for j in range(i):
                if DP[j] and A[j] + j >= i:
                    DP[i] = True
                    break
                
        return DP[n - 1]
