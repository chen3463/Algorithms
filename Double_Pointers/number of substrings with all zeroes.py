'''
Given a string str containing only0 or 1, please return the number of substrings that are consist of 0 .

Example
Example 1:

Input:"00010011"
Output:9
Explanation:
There are 5 substrings of "0",
There are 3 substrings of "00",
There is 1 substring of "000".
So return 9
Example 2:

Input:"010010"
Output:5
Notice
1<=|str|<=30000
'''

class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def stringCount(self, str):
        # Write your code here.
        j = 0
        CNT = 0
        for i in range(len(str)):
            if str[i] == '0':
                CNT += (j + 1)
                j += 1
            else:
                j = 0
        
        
        return CNT
