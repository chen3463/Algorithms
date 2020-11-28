'''
5. Kth Largest Element

Find K-th largest element in an array.

Example

Example 1:

Input:
n = 1, nums = [1,3,4,2]
Output:
4
Example 2:

Input:
n = 3, nums = [9,3,2,4,8]
Output:
4
Challenge

O(n) time, O(1) extra memory.

Notice

You can swap elements in the array
'''


class Solution1:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums:
            return -1
        
        return self.QuickSelect(nums, 0, len(nums) - 1, n)
        
    
    def QuickSelect(self, nums, start, end, n):
        # print(nums)
        if start == end:
            return nums[start]
        
        i, j = start, end
        pivot = nums[(j - i) // 2 + i]
        
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1 
                
            while i <= j and nums[j] < pivot:
                j -= 1 
                
            if i <= j:    
                nums[i], nums[j] = nums[j], nums[i]
              
                i += 1 
                j -= 1

        if start + n - 1 <= j:
            return self.QuickSelect(nums, start, j, n)
            
        if start + n - 1 >= i:
            return self.QuickSelect(nums, i, end, n - (i - start))
        
        return nums[i - 1]

class Solution2:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
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
            while left <= right and nums[left] > p:
                left += 1 
            while left <= right and nums[right] < p:
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
