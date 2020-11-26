'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Example

Example 1

Input : [1, 0, 1, 2]
Output : [0, 1, 1, 2]
Explanation : sort it in-place
Challenge

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

Notice

You are not suppose to use the library's sort function for this problem.
You should do it in-place (sort numbers in the original array).
'''


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return nums
        
        # print(nums)    
        self.partition(nums, 0, len(nums) - 1, 0.5)
        # print(nums)
        self.partition(nums, 0, len(nums) - 1, 1.5)
        # print(nums)
        
        
    def partition(self, nums, left, right, p):
        
        while left <= right:
            while left <= right and nums[left] < p:
                left += 1 
            while left <= right and nums[right] > p:
                right -= 1 
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1 
                
