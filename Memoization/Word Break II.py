/*
DescriptionSolutionNotesDiscussLeaderboard
Description
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Example
Example 1:

Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".
Example 2:

Input："a"，[]
Output：[]
Explanation：dict is null.

*/

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.memo_search(s, wordDict, {})

    def memo_search(self, s, wordDict, memo):
        if len(s) == 0:
            return ['']

        if s in memo:
            return memo[s]

        partitions = []
        for i in range(1, len(s)):
            prefix = s[: i]
            if prefix not in wordDict:
                continue
            for partition in self.memo_search(s[i :], wordDict, memo):
                partitions.append(prefix + " " + partition)

        if s in wordDict:
            partitions.append(s)
        
        memo[s] = partitions

        return memo[s]
