

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return []

        candidates = sorted(set(candidates))
        results = []
        self.dfs(candidates, 0, target, [], results)
        return results

    def dfs(self, candidates, index, target, result, results):
        if target < 0:
            return

        if target == 0:
            return results.append(list(result))

        for i in range(index, len(candidates)):
            result.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], result, results)
            result.pop()

    # time O(n ** (target / min of set))
    # space O(n ** (target / min of set))
