'''


Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
Example  1:
	Input: tree = {1,2,3}
	Output: true
	
	Explanation:
	This is a balanced binary tree.
		  1  
		 / \                
		2  3

	
Example  2:
	Input: tree = {3,9,20,#,#,15,7}
	Output: true
	
	Explanation:
	This is a balanced binary tree.
		  3  
		 / \                
		9  20                
		  /  \                
		 15   7 

	
Example  3:
	Input: tree = {1,#,2,3,4}
	Output: false
	
	Explanation:
	This is not a balanced tree. 
	The height of node 1's right sub-tree is 2 but left sub-tree is 0.
		  1  
		   \                
		   2                
		  /  \                
		 3   4
	
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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        balanced, _ = self.valid(root)
        
        return balanced
        
    def valid(self, root):
        if root is None:
            return True, 0
            
        balance_left, depth_left = self.valid(root.left)
        if not balance_left:
            return False, 0
        balance_right, depth_right = self.valid(root.right)
        if not balance_right:
            return False, 0
        
        return abs(depth_left - depth_right) <= 1, max(depth_left, depth_right) + 1
