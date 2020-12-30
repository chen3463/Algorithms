'''

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree: root = {6,2,8,0,4,7,9,#,#,3,5}

Example
Example 1:

Input: 
{6,2,8,0,4,7,9,#,#,3,5}
2
8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: 
{6,2,8,0,4,7,9,#,#,3,5}
2
4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Notice
All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
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
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
            
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        else:
            return root
