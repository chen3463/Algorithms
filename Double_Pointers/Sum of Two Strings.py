'''
1343. Sum of Two Strings

Given you two strings which are only contain digit character. you should return the sum of each digit as string

Example
Example1:
Input:
A = "99"
B = "111"
Output: "11010"
Explanation: because 9 + 1 = 10, 9 + 1 = 10, 0 + 1 = 1,connect them，so answer is "11010"
Example2:
Input:
A = "2"
B = "321"
Output: "323"
Explanation: because 2 + 1 = 3, 2 + 0 = 2, 3 + 0 = 3, connect them，so answer is "323"
Notice
A and B are strings which are composed of numbers
'''

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        indexA = len(A) - 1 
        indexB = len(B) - 1 
        result = ""
        while indexA >= 0 and indexB >= 0:
            temp = ord(A[indexA]) + ord(B[indexB]) - 2 * ord('0')
            result = str(temp) + result
            indexA -= 1 
            indexB -= 1 
        if len(A) > len(B):
            result = A[: indexA + 1] + result
        else:
            result = B[: indexB + 1] + result
            
        return result
