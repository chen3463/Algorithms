'''
31. Partition Array

Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example

Example 1:

Input:
[],9
Output:
0

Example 2:

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1
Challenge

Can you partition the array in-place and in O(n)?

Notice

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length
'''

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
        
        left, right = 0, len(nums) - 1 
        
        while left < right:
            while left <= right and nums[left] < k:
                left += 1 
            while left <= right and nums[right] >= k:
                right -= 1 
            
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
                
        return left
