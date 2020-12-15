'''
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.


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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.min_subsum = float('inf')
        self.min_subsum_root = None
        
        self.get_subsum(root)
        
        return self.min_subsum_root
        
    def get_subsum(self, root):
        if root is None:
            return 0
        
        left_val = self.get_subsum(root.left)
        right_val = self.get_subsum(root.right)
        root_sum = left_val + root.val + right_val
        if root_sum < self.min_subsum:
            self.min_subsum_root = root
            self.min_subsum = root_sum
        return root_sum
