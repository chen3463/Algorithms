class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if not A:
            return []
        
        A.sort()
        results = []
        self.dfs(A, k, target, 0, [], results)
        return results

    def dfs(self, A, k, target, index, result, results):
        if target < 0 or k < 0:
            return

        if target == 0 and k == 0:
            return results.append(list(result))

        for i in range(index, len(A)):
            result.append(A[i])
            self.dfs(A, k - 1, target - A[i], i + 1, result, results)
            result.pop()
