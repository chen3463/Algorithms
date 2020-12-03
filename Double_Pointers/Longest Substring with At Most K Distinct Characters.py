'''
Longest Substring with At Most K Distinct Characters

Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Example
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"
Challenge
O(n) time

'''
class Solution1:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s:
            return 0
            
        left, answer = 0, 0
        counter = {}
        n = len(s)
        for right in range(n):
            counter[s[right]] = counter.get(s[right], 0) + 1 
            while left <= right and len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1 
        
            answer = max(answer, right - left + 1)
        
        return answer
    
class Solution2:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        counter = {}
        CNT = 0
        left = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while left <= right and len(counter) == k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            if len(counter) == k - 1 and left > 0:
                CNT += left
        
        return CNT
