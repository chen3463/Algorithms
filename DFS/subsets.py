/*
Description
Given a set with distinct integers, return all possible subsets.

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Example
Example 1:

Input:

nums = [0]
Output:

[
[],
[0]
]
Explanation:

The subsets of [0] are only [] and [0].

Example 2:

Input:

nums = [1,2,3]
Output:

[
[3],
[1],
[2],
[1,2,3],
[1,3],
[2,3],
[1,2],
[]
]
Explanation:

The subsets of [1,2,3] are [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].

Challenge
Can you do it in both recursively and non-recursively?


*/

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums is None:
            return None
        nums.sort()
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums is None:
            return None
        nums.sort()
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, i, combination, combinations):
        if i == len(nums):           
            combinations.append(list(combination))
            return

        combination.append(nums[i])
        self.dfs(nums, i + 1, combination, combinations)
        combination.pop()
        self.dfs(nums, i + 1, combination, combinations)
