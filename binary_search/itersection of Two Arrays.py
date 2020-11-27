'''
Given two arrays, write a function to compute their intersection.

Example
Example 1:

Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2], 
Output: [2].
Example 2:

Input: nums1 = [1, 2], nums2 = [2], 
Output: [2].
Challenge
Can you implement it in three different algorithms?

Notice
Each element in the result must be unique.
The order of the results needs to be ascending
'''

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        if not nums1 or not nums2:
            return []
            
        ans = []
        counter1 = {}
        counter2 = {}
        
        for n in nums1:
            counter1[n] = counter1.get(n, 0) + 1 
        
        for n in nums2:
            counter2[n] = counter2.get(n, 0) + 1 
        
        counter = {}    
        for n in list(counter1.keys()) + list(counter2.keys()):
            counter[n] = counter.get(n, 0) + 1 
            if counter[n] == 2:
                ans.append(n)
        
        return ans
