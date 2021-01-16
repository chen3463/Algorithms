/*
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

Example
Example1

Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"
Example1

Input:
"a"
[]
Output: 
0
Notice
Ignore case
*/

class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dictionary):
        # Write your code here
        dict_low = self.init_dict(dictionary)
        return self.DP_search(s.lower(), dict_low)
        
    def DP_search(self, s, dictionary):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if s[i : j + 1] in dictionary:
                    dp[i][j] = 1

        for i in range(n):
            for j in range(i, n):
                for k in range(i, j):
                    dp[i][j] += dp[i][k] * dp[k + 1][j]
        
        return dp[0][n - 1]
        
        
        
    def init_dict(self, dictionary):
        dict_low = set()
        for word in dictionary:
            dict_low.add(word.lower())
            
        return dict_low
        
    
        


class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """
    # DP[i] means wasys to s[0:i]
    def wordBreak3(self, s, dict):
        # Write your code here
        if not s or not dict:
            return 0
        dict_lower = self.lower_dict(dict)
        s = s.lower()
        n = len(s)    
        DP = [0] * (n + 1)
        DP[0] = 1
        for i in range(n):
            for j in range(i, n):
                if s[i : j + 1] in dict_lower:
                    DP[j + 1] += DP[i]
        return DP[n]
        
    def lower_dict(self, dict):
        dict_lower = set()
        for word in dict:
            dict_lower.add(word.lower())
            
        return dict_lower
        
