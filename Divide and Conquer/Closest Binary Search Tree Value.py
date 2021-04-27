/*
Description
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example
Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1
*/

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        result = root.val
        while root:
            if abs(root.val - target) < abs(result - target):
                result = root.val

            if target < root.val:
                root = root.left

            elif target > root.val:
                root = root.right

            else:
                return root.val

        return result
        
        
 
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        upper = self.get_upper(root, target)
        lower = self.get_lower(root, target)

        if upper is None and lower is not None:
            return lower.val

        if upper is not None and lower is None:
            return upper.val

        if upper is None and lower is None:
            return None

        # print(lower.val, upper.val)
        if target - lower.val < upper.val - target:
            return lower.val

        else:
            return upper.val

    def get_lower(self, root, target):
        if not root:
            return None

        if target < root.val:
            return self.get_lower(root.left, target)

        left = self.get_lower(root.right, target)

        return left or root 

    def get_upper(self, root, target):
        if not root:
            return None

        if target >= root.val:
            return self.get_upper(root.right, target)

        right = self.get_upper(root.left, target)

        return right or root
