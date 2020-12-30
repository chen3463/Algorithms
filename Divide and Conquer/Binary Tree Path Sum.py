'''
Binary Tree Path Sum

Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Example
Example 1:

Input:
{1,2,4,2,3}
5
Output: [[1, 2, 2],[1, 4]]
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        path = []
        results = []
        length = 0
        self.DFS(root, path, results, length, target)
        
        return results
            
    def DFS(self, root, path, results, length, target):
        if root is None:
            return 
        
        path.append(root.val)
        length += root.val
        if root.left is None and root.right is None and length == target:
            results.append(path[:])
        self.DFS(root.left, path, results, length, target)
        self.DFS(root.right, path, results, length, target)
        
        path.pop()
