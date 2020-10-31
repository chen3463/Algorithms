'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.mininumn = sys.maxsize
        self.traverse(triangle, 0, 0, 0)
        return self.mininumn
    
    def traverse(self, triangle, x, y, sub_path_sum):
       if len(triangle) == x:
           self.mininumn = min(sub_path_sum, self.mininumn)
           return 
       
       self.traverse(triangle, x + 1, y, sub_path_sum + triangle[x][y])
       self.traverse(triangle, x + 1, y + 1, sub_path_sum + triangle[x][y])
 
class Solution2:
   def minimumTotal(self, triangle: List[List[int]]) -> int:
       return self.devide_conquer(triangle, 0, 0)
        
    
   def devide_conquer(self, triangle, x, y):
       if len(triangle) == x:
           return 0
       
       left = self.devide_conquer(triangle, x + 1, y) 
       right = self.devide_conquer(triangle, x + 1, y + 1)
       return min(left, right) + triangle[x][y]
       
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.devide_conquer(triangle, 0, 0, {})
        
    
    def devide_conquer(self, triangle, x, y, memo):
        if len(triangle) == x:
            return 0
        
        if (x, y) in memo.keys():
            return memo[(x, y)]
            
        left = self.devide_conquer(triangle, x + 1, y, memo) 
        right = self.devide_conquer(triangle, x + 1, y + 1, memo)
        memo[(x, y)] = min(left, right) + triangle[x][y]
            
        return memo[(x, y)]
