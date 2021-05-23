'''
Stretch Word
Algorithms
Easy
Accepted Rate
35%

DescriptionSolutionNotesDiscussLeaderboard
Description
Given a string, you can get a new string by manipulating the same consecutive characters in the string. You are only allowed to do the following: Keep 1 or 2 characters of the same character whose continuous times are greater than or equal to 2, and delete the rest.

You have to make sure that there are no more than two consecutive identical characters in the new string. If the input string meets the requirements, you don't need to do anything with it.
'''

class Solution:
    """
    @param S: the string
    @return: The numbers of strings
    """
    def stretchWord(self, S):
        # write your code here
        if not S:
            return 0

        answer = 1
        index = 0
        while index < len(S) - 1:
            current_count = 1
            while index < len(S) - 1 and S[index] == S[index + 1]:
                current_count += 1
                index += 1
            if current_count > 1:
                answer *= 2
            
            index += 1

        return answer
