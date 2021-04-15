/*
Description
Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the terminating number is not found, return -1.

Example
Example1

Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
5
Output: 3
Example2

Input: 
[1, 2, 2, 1, 3, 4, 4, 5, 6]
7
Output: -1
Example3

Input: 
[1, 2, 2, 1, 3, 4]
3
Output: 3
*/

class Solution1:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here

        hash_num = {}

        for i, num in enumerate(nums):
            hash_num[num] = hash_num.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1
        
        for i, num in enumerate(nums):
            if hash_num[num] == 1:
                return num
            
            if hash_num[num] == number:
                break

        return -1

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 
        self.prev = None

class Solution2:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        self.initialize()
        val_node = {}
        found = False
        for num in nums:
            if num not in val_node:
                node = Node(num)
                val_node[num] = node
                self.add_new(node)

            else:
                if val_node[num]:
                    node = val_node[num]
                    self.remove(node)
                    val_node[num] = None

            if num == number:
                found = True
                break 

        if not found:
            return -1
        
        return self.head.next.val

    def initialize(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_new(self, node):
        pre_node = self.tail.prev
        next_node = self.tail
        pre_node.next = node
        node.prev = pre_node
        node.next = next_node
        next_node.prev = node
         
        
    
    def remove(self, node):
        pre_node = node.prev
        next_node = node.next 
        pre_node.next = next_node
        next_node.prev = pre_node

        
