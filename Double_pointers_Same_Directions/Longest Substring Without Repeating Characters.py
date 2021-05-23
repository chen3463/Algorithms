/*
Description
Given a string, find the length of the longest substring without repeating characters.

Example
Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The longest substring is "abc".
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The longest substring is "b".
Challenge
time complexity O(n)
*/

class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if not s:
            return 0

        longest = 0
        num_to_index = {}
        start_index = 0
        for i, num in enumerate(list(s)):
            if num in num_to_index and num_to_index[num] >= start_index:               
                start_index = num_to_index[num] + 1

            num_to_index[num] = i

            if longest < i - start_index + 1:
                longest = i - start_index + 1

        return longest
