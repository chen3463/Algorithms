'''

Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.
Challenge
Do it in-place and without extra memory.

Notice
You are not necessary to keep the original order of positive integers or negative integers.
'''
class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        n = len(A)
        pos, neg = 0, 0
        
        for i in range(len(A)):
            if A[i] > 0:
                pos += 1 
            else:
                neg += 1
            
        
        self.partition(A, 0, n - 1, pos < neg)
        # print(A)
        self.switch(A, n, 1, n - 1)
            
    def partition(self, A, left, right, start_with_positive):
        flag = 1 if start_with_positive else -1
        while left <= right:
            while left <= right and A[left] * flag < 0:
                left += 1 
                
            while left <= right and A[right] * flag > 0:
                right -= 1 
                
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1 
                right -= 1 
        
            
    def switch(self, A, n, left, right):
        
        if n % 2 == 0:
            right = right - 1 
            
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 2 
            right -= 2
