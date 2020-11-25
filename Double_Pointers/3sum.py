'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
'''

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers:
            return []
            
        numbers = sorted(numbers)
        
        results = []
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            target = 0 - numbers[i]
            
            left, right = i + 1, len(numbers) - 1 
            
            while left < right:
                if numbers[left] + numbers[right] == target:
                    results.append([numbers[i], numbers[left], numbers[right]])
                    left += 1 
                    right -= 1 
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1 
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1 
                    
                elif numbers[left] + numbers[right] < target:
                    left += 1 
                    
                else:
                    right -= 1 
                    
        return results
