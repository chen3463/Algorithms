'''
607. Two Sum III - Data structure design

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
Example 1:

add(1); add(3); add(5);
find(4) // return true
find(7) // return false
'''

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.number_list = []
        
    def add(self, number):
        # write your code here
        self.number_list.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        num_dict = {}
        print(self.number_list)
        n = len(self.number_list)
        for i in range(n):
            if (value - self.number_list[i]) not in num_dict.keys():
                num_dict[self.number_list[i]] = i 
                
            else:
                return True
        
        return False    
