/*

*/


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []

        keyboard = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        results = []
        self.dfs(digits, 0, [], results, keyboard)
        return results

    def dfs(self, digits, index, result, results, keyboard):
        if len(result) == len(digits):
            return results.append(''.join(result))
      
        for char in keyboard[digits[index]]:
            result.append(char)
            self.dfs(digits, index + 1, result, results, keyboard)
            result.pop()
            
    # time O(4 ** n)    
    # space O(4 ** n)
