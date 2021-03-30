'''
Kth Smallest Element in a BST
中文English
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example
Example 1:

Input：{1,#,2},2
Output：2
Explanation：
1
 \
  2
The second smallest element is 2.
Example 2:

Input：{2,1,3},1
Output：1
Explanation：
 2
/ \
1 3
The first smallest element is 1.
Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Notice
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        self.count = 0
        self.result = 0
        self.InOrderTraversal(root, k)       
        return self.result

    def InOrderTraversal(self, root, k):
        if root is None:
            return
        
        self.InOrderTraversal(root.left, k)
        self.count += 1

        if self.count == k:
            self.result = root.val

        self.InOrderTraversal(root.right, k)
        
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for _ in range(k):
            node = stack.pop()
            if node:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack is None:
                return None
        
        return stack[-1].val
