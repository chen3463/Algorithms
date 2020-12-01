
'''
Given an array of integers, remove the duplicate numbers in it.

You should:

Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.
Example
Example 1:

Input:
nums = [1,3,1,4,4,2]
Output:
[1,3,4,2,?,?]
4
Explanation:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.
Example 2:

Input:
nums = [1,2,3]
Output:
[1,2,3]
3
Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.
Notice
You don't need to keep the original order of the integers.
'''

class Solution1:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
        nums.sort()
        i = 0
        for j in range(1, len(nums)):
            if nums[j] > nums[i]:
                i += 1
                nums[i] = nums[j]
                
        
        return i + 1
        
class Solution2:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0
        counter = {}
        j = 0
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
            # print(i, j, counter[nums[j]])
            if counter[nums[i]] == 1:
                nums[j] = nums[i]
                j += 1
        
        return j
