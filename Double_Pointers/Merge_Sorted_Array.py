'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Example
Example 1:

Input：[1, 2, 3] 3  [4,5]  2
Output：[1,2,3,4,5]
Explanation:
After merge, A will be filled as [1, 2, 3, 4, 5]
Example 2:

Input：[1,2,5] 3 [3,4] 2
Output：[1,2,3,4,5]
Explanation:
After merge, A will be filled as [1, 2, 3, 4, 5]
Notice
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. 
The number of elements initialized in A and B are m and n respectively.
'''

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        
        i, k, j = m + n - 1, m - 1, n - 1
        while k >= 0 and j >= 0:
            if A[k] > B[j]:
                A[i] = A[k]
                k -= 1
            else:
                A[i] = B[j]
                j -= 1 
            i -= 1 
            
        while k >= 0:
            A[i] = A[k]
            i -= 1 
            k -= 1
         
        
        while j >= 0:
            A[i] = B[j]
            i -= 1
            j -= 1
