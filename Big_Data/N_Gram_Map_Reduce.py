'''
Description

Give a number of strings and the number N. Use the Map Reduce method to count all N-Grams and their occurrences. The letter is granular.
Have you met this question in a real interview?  Yes
Problem Correction
Example
Example 1:

Input: N = 3
doc_1: "abcabc"
doc_2: "abcabc"
doc_3: "bbcabc"
Output:
[
  "abc": ５,
  "bbc": 1, 
  "bca": 3,
  "cab": 3
]
Example 2:

Input: N=3
doc_1: "abcabc"
Output:
[
  "abc": 2, 
  "bca": 1,
  "cab": 1
]
'''

class NGram:

    # @param {int} n a integer
    # @param {str} string a string
    def mapper(self, _, n, string):
        # Write your code here
        # Please use 'yield key, value' here
        length = len(string)
        for start in range(length - n + 1):
            yield string[start : start + n], 1 
        


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        yield key, sum(values)
