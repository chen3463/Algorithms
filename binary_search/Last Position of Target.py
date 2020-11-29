'''
Find the last position of a target number in a sorted array. Return -1 if target does not exist.

Example
Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
'''

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1 
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if target >= nums[mid]:
                left = mid
            else:
                right = mid
        
        if nums[right] == target:
            return right
        
        if nums[left] == target:
            return left
        
        return -1
