/*
Description
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Example
Example 1:

Input the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output: 11
Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Example 2:

Input the following triangle:
[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
Output: 12
Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).
*/

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return None

        n, m = len(triangle), len(triangle[-1])
        DP = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        DP[-1] = triangle[-1]
        for i in range(-2, - n - 1, -1):
            for j, num in enumerate(triangle[i]):
                DP[i][j] = triangle[i][j] + min(DP[i + 1][j], DP[i + 1][j + 1])

        return DP[0][0]
