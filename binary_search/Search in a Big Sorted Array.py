'''
Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example
Example 1:

Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1
Example 2:

Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
Challenge
O(logn) time, n is the first index of the given target number.

Notice
If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.
'''

class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        left = 0
        right = self.find_right(reader, 1, target)
            
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if reader.get(mid) < target:
                left = mid
            else:
                right = mid
        
        if reader.get(left) == target:
            return left
        
        if reader.get(right) == target:
            return right
        
        return -1
        
    def find_right(self, reader, right, target):
        while reader.get(right) < target and reader.get(right) < 2147483647:
            right = right * 2
        return right
