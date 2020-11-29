'''
Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example
Example 1:

Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.
Example 2:

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.
Notice
You can assume no duplicate exists in the array.
'''

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        return self.binary_search(nums, 0, len(nums) - 1)
        
    def binary_search(self, nums, left, right):
        
        while left + 1 < right:
            mid = (right - left) // 2 + left 

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        if left == right:
            return nums[left]
        
        if nums[left] < nums[right]:
            return nums[left]
            
        else:
            return nums[right]
