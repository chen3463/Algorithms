'''

DescriptionConsoleNote

Find any position of a target number in a sorted array. Return -1 if target does not exist.

Example

Example 1:

Input: nums = [1,2,2,4,5,5], target = 2
Output: 1 or 2
Example 2:

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
Challenge

O(logn) time
'''

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
            
        start = 0
        end = len(nums) - 1 
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
                
            if nums[mid] > target:
                end = mid - 1
                
            if nums[mid] < target:
                start = mid + 1 
        
        if target == nums[start]:
            return start 
                
        
        if target == nums[end]:
            return end 
                
        return -1
