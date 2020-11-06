'''
Word count
Using map reduce to count word frequency.

https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html#Example%3A+WordCount+v1.0

Example

Example 1:

Input:
    chunk1: "Google Bye GoodBye Hadoop code"
    chunk2: "lintcode code Bye"

Output:
    Bye: 2
    GoodBye: 1
    Google: 1
    Hadoop: 1
    code: 2
    lintcode: 1
Example 2:

Input:
    chunk1: "Lintcode is so so good"

Output:
    Lintcode: 1
    good: 1
    is: 1
    so: 2
'''



class WordCount:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        for word in line.split(" "):
            yield word, 1


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        yield key, sum(values)
