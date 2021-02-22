/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Example
Example 1:

Input:  {-1}
Output：true
Explanation：
For the following binary tree（only one node）:
	      -1
This is a binary search tree.
Example 2:

Input:  {2,1,4,#,#,3,5}
Output: true
For the following binary tree:
	  2
	 / \
	1   4
	   / \
	  3   5
This is a binary search tree.
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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        return self.validate(root, -sys.maxsize, sys.maxsize)
    
    def validate(self, root, lower, upper):
        if root is None:
            return True
            
        if root.val <= lower or root.val >= upper:
            return False
        
        return self.validate(root.left, lower, root.val) and self.validate(root.right, root.val, upper)

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        self.isValid = True
        self.lastVal = None
        self.validate(root)
        return self.isValid
        
    def validate(self, root):
        if root is None:
            return
        
        self.validate(root.left)
        
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isValid = False
            return 
        
        self.lastVal = root.val   
        self.validate(root.right)
        
        
