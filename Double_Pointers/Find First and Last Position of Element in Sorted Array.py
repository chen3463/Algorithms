'''
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    """
    @param nums: the array of integers
    @param target: 
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        if not nums:
            return [-1, -1]
            
        left, right = 0, len(nums) - 1 
        
        return [self.find_left(nums, left, right, target), self.find_right(nums, left, right, target)]
        
    def find_left(self, nums, left, right, target):
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if target <= nums[mid]:
                right = mid
            
            else:
                left = mid
            
        if nums[left] == target:
            return left
        
        if nums[right] == target:
            return right
        
        return -1
            
    def find_right(self, nums, left, right, target):
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
