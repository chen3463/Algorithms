/*
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.

*/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        nums.sort()
        n = len(nums)
        DP = [1 for _ in range(n)]
        PR = [-1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and DP[i] < DP[j] + 1:
                    DP[i] = DP[j] + 1
                    PR[i] = j
        longest, last_index = 0, -1
        for i in range(n):
            if longest < DP[i]:
                longest = DP[i]
                last_index = i

        path = []
        while last_index != -1:
            path.append(nums[last_index])
            last_index = PR[last_index]
            
        return path[::-1]
        
class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        if not nums:
            return None

        nums.sort()
        DP, PR = {}, {}
        for num in nums:
            DP[num], PR[num] = 1, -1
        last_num = nums[0]
        for num in nums:
            for factor in self.get_factors(num):
                if factor not in DP:
                    continue
                if DP[factor] + 1 > DP[num]:
                    DP[num] = DP[factor] + 1
                    PR[num] = factor

            if DP[num] > DP[last_num]:
                last_num = num

        return self.get_path(PR, last_num)

    def get_path(self, PR, last_num):
        path = []
        while last_num != -1:
            path.append(last_num)
            last_num = PR[last_num]
        return path[::-1]

    def get_factors(self, num):
        if num == 1:
            return []
        factors = []
        factor = 1
        while factor ** 2 <= num:
            if num % factor == 0:
                factors.append(factor)
                if factor ** 2 < num and factor != 1:
                    factors.append(num // factor)
            factor += 1

        return factors
