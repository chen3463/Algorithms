'''
1870. number of substrings with all zeroes

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
        if not str:
            return 0 
            
        j, CNT = 1, 0
        n = len(str)

        for i in range(n):
            if str[i] != "0":
                continue
            j = max(j, i + 1)
            print(i, j)
            while j < n and str[j] == "0":
                j += 1 
                
            CNT += j - i 
        
        return CNT 
