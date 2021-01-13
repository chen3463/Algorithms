'''
539. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example

Example 1:

Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].
Example 2:

Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
Notice

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return 
        n = len(nums)
        left = 0
        right = 0
        while right < n:
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1 
                
            right += 1
            
        while left < n:
            if nums[left] != 0:
                nums[left] = 0 
            left += 1    
            
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1          
