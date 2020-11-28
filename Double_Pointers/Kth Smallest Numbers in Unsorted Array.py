'''
Find the kth smallest number in an unsorted integer array.

Example
Example 1:

Input: [3, 4, 1, 2, 5], k = 3
Output: 3
Example 2:

Input: [1, 1, 1], k = 2
Output: 1
Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
'''

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        if not nums:
            return 
        
        return self.quick_select(k - 1, nums, 0, len(nums) - 1)
        
    def quick_select(self, k, nums, start, end):
        if start == end:
            return nums[start]
        
        left, right = start, end
        p = (nums[left] + nums[right]) / 2
        while left <= right:
            while left <= right and nums[left] < p:
                left += 1 
            while left <= right and nums[right] > p:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1
                
        if right >= k and start <= right:
            return self.quick_select(k, nums, start, right)
            
        elif k >= left and left <= end:
            return self.quick_select(k, nums, left, end)
            
        else:
            return nums[k]
                
        
        
        
