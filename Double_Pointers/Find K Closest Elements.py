'''
Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Example 1:

Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
Challenge
O(logn + k) time

Notice
The value k is a non-negative integer and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^410
​4
​​ 
Absolute value of elements in the array will not exceed 10^410
​4
​​
'''

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if len(A) < k or k == 0:
            return []
        n = len(A)
        ans = []
        right = self.find_right_close(A, 0, n - 1, target)
        left = right - 1
        for _ in range(k):
            if self.left_is_close(A, left, right, target):
                ans.append(A[left])
                left -= 1
            else:
                ans.append(A[right])
                right += 1
                
        return ans
        
        
    def find_right_close(self, A, left, right, target):
        while left + 1 < right:
            mid = (right - left) // 2 + left 
            if target <= A[mid]:
                right = mid
            else:
                left = mid
    
        if A[left] >= target:
            return left 
        if A[right] >= target:
            return right
        
        return len(A)
            
    def left_is_close(self, A, left, right, target):
        if left < 0:
            return False
        if right >= len(A):
            return True
        
        return target - A[left] <= A[right] - target
