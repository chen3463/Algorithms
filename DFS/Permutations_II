class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None:
            return None

        nums.sort()
        results = []
        visited = [False for _ in range(len(nums))]
        self.dfs(nums, 0, [], results, visited)
        return results

    def dfs(self, nums, index, result, results, visited):
        if len(nums) == len(result):
            return results.append(list(result))
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            result.append(nums[i])
            self.dfs(nums, i, result, results, visited)
            result.pop()
            visited[i] = False

