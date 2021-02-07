'''
Given a collection of intervals, merge all overlapping intervals.

Example
Example 1:

Input: [(1,3)]
Output: [(1,3)]
Example 2:

Input:  [(1,3),(2,6),(8,10),(15,18)]
Output: [(1,6),(8,10),(15,18)]
Challenge
O(n log n) time and O(1) extra space.
'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def get_start(self, interval):
        return interval.start
        
    def merge(self, intervals):
        # write your code here
        intervals = sorted(intervals, key = self.get_start)
        results = []
        for interval in intervals:
            if results == [] or results[-1].end < interval.start:
                results.append(interval)
            else:
                if results[-1].end < interval.end:
                    results[-1].end = interval.end
                else:
                    continue
        return results
