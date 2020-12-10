

'''
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
Example
Example 1:

Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：2
Explanation：
"a"->"c"
Example 2:

Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：5
Explanation：
"hit"->"hot"->"dot"->"dog"->"cog"
Notice
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        visited = set([start])
        queue = collections.deque([start])
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
            
                for next_word in self.get_words(word):
                    if next_word in visited or next_word not in dict:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
                    
        return 0
    
    def get_words(self, word):
        words = []
        for i in range(len(word)):
            start, end = word[:i], word[i + 1:]
            for mid in 'abcdefghijklmnopqrstuvwxyx':
                words.append(start + mid + end)
        return words
                
