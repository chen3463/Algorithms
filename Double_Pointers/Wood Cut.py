'''
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Example
Example 1

Input:
L = [232, 124, 456]
k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
Example 2

Input:
L = [1, 2, 3]
k = 7
Output: 0
Explanation: It is obvious we can't make it.
Challenge
O(n log Len), where Len is the longest length of the wood.

Notice
You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.
'''
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
            
        left, right = 1, sum(L) // k
        
        while left + 1 < right:
            mid = (right - left) // 2 + left 
            N = sum([num // mid for num in L])
            if N < k:
                right = mid
            elif N >= k:
                left = mid
        
        N_right = sum([num // right for num in L])  
        if N_right >= k:
            return right
        
        N_left = sum([num // left for num in L])        
        if  N_left >= k:
            return left
            
        return 0
