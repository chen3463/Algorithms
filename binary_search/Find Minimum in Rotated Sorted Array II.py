/*
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example

Example 1:

Input :[2,1]
Output : 1.
Example 2:

Input :[4,4,5,6,7,0,1,2]
Output : 0.
Notice

The array may contain duplicates.
*/

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[right]:
                left = mid
            
            elif nums[mid] < nums[right]:
                right = mid
            
            else:
                right -= 1
                
        if nums[left] <= nums[right]:
            return nums[left]
            
        else:
            return nums[right]
