class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, nums):
        # write your code here
        if not nums:
            return
        
        self.quick_sort(nums, 0, len(nums) - 1) 
        
    def quick_sort(self, nums, start, end):
        if start >= end:
            return 
        left, right = start, end 
        
        mid = (right - left) // 2 + left
        p = nums[mid]
        
        while left <= right:
            while left <= right and nums[left] < p:
                left += 1 
            while left <= right and nums[right] > p:
                right -= 1 
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1
                
        
        self.quick_sort(nums, start, right)
        self.quick_sort(nums, left, end)
