class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if nums is None:
            return None

        nums.sort()
        results = []
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums, index, result, results):
        results.append(list(result))
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            result.append(nums[i])
            self.dfs(nums, i + 1, result, results)
            result.pop()
