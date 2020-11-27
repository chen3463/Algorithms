'''
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Example
Example1

Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]
Example2

Input: 
[2,1,1,2,2] 
2
Output: 
[1,1,2,2,2]
Challenge
A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?

Notice
You are not suppose to use the library's sort function for this problem.
k <= n
'''


class Solution1:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
 
        for i in range(1, k):
            # print((2 * i + 1) / 2.0)
            
            self.swap(colors, 0, len(colors) - 1,  (2 * i + 1) / 2.0)
            
            # print(colors)
            
    def swap(self, colors, left, right, p):
        while left <= right:
            while left <= right and colors[left] < p:
                left += 1  
            while left <= right and colors[right] > p:  
                right -= 1
            
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1 
                right -= 1 
                
class Solution2:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        self.partition_sort(colors, 1, k, 0, len(colors) - 1)
        
    def partition_sort(self, colors, from_color, to_color, index_from, index_to):
        if from_color == to_color or from_color == to_color:
            return
        
        left, right = index_from, index_to
        color = (from_color + to_color) // 2 
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1 
            while left <= right and colors[right] > color:
                right -= 1 
                
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1 
                right -= 1 
        self.partition_sort(colors, from_color, color, index_from, right)
        self.partition_sort(colors, color + 1, to_color, left, index_to)
