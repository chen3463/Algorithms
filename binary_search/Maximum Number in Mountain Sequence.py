'''
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Example
Example 1:

Input: nums = [1, 2, 4, 8, 6, 3] 
Output: 8
Example 2:

Input: nums = [10, 9, 8, 7], 
Output: 10
Notice
Arrays are strictly incremented, strictly decreasing
'''

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        
        left, right = 0, len(nums) - 1 
        
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if nums[mid] < nums[mid + 1]:
                left = mid
            
            elif nums[mid] > nums[mid + 1]:
                right = mid
                
        if nums[left] >= nums[right]:
            return nums[left]
        else:
            return nums[right]
