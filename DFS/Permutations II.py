/*
Description
Given a list of numbers with duplicate numbers in it. Find all unique permutations of it.

Example
Example 1:

Input:

nums = [1,1] 
Output:

[ 
  [1,1] 
] 
Explanation:

The different arrangement of [1,1] is only [1,1].

Example 2:

Input:

nums = [1,2,2] 
Output:

[ 
  [1,2,2], 
  [2,1,2], 
  [2,2,1] 
] 
Explanation:

The different arrangements of [1,2,2] are [1,2,2],[2,1,2]and [2,2,1].

Challenge
Using recursion to do it is acceptable. If you can do it without recursion, that would be great!
*/

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if nums is None:
            return None

        nums.sort()
        visited = [False for _ in range(len(nums))]
        permutations = []
        self.dfs(nums, [], permutations, visited)
        return permutations
    
    def dfs(self, nums, permutation, permutations, visited):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, permutation, permutations, visited)
            permutation.pop()
            visited[i] = False
