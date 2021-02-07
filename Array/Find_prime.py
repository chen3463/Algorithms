'''

'''
class Solution:
    """
    @param n: an integer
    @return: return all prime numbers within n.
    """
    def prime(self, n):
        # write your code here
        if n < 2:
            return []
        
        if n == 2:
            return [2]
            
        results = [2]
        
        for num in range(3, n + 1):
            for result in results:
                if num % result == 0:
                    IsPrime = False
                    break
                else:
                    IsPrime = True
                    
            if IsPrime:
                results.append(num)
                
        
        return results
