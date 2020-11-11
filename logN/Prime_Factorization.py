'''
Prime Factorization

Prime factorize a given integer.

Example
Example 1:

Input: 10
Output: [2, 5]
Example 2:

Input: 660
Output: [2, 2, 3, 5, 11]
Notice
You should sort the factors in ascending order.
'''
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        up = int(math.sqrt(num))
        # print(up)
        results = []
        k = 2
        while k <= up and num > 1:
            while num % k == 0:
                num = num // k 
                results.append(k)
            k += 1 
        
        if num > 1:
            results.append(num)
            
        return results
