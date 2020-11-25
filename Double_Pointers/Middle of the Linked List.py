'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example

Example 1:

Input: 1->2->3->4->5->null
Output: 3->4->5->null
Example 2:

Input: 1->2->3->4->5->6->null
Output: 4->5->6->null
Notice

The number of nodes in the given list will be between 1 and 100.
'''

class Solution:
    """
    @param head: the head node
    @return: the middle node
    """
    def middleNode(self, head):
        # write your code here.
        slow = head
        fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            return slow.next
        else:
            return slow
