/*
Description
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

Ignore case

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

*/


class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        WordDict, longest = self.init(dict)
        print(WordDict, longest)
        return self.memo_search(s.lower(), 0, WordDict, longest, {})

    def init(self, WordDict):
        new_words, longest = set(), 0
        for word in WordDict:
            new_words.add(word.lower())
            if longest < len(word):
                longest = len(word)
        
        return list(new_words), longest

    def memo_search(self, s, index, WordDict, max_length, memo):
        if len(s) == index:
            return 1
        
        if index in memo:
            return memo[index]

        memo[index] = 0
        for i in range(index, len(s)):
            if i + 1 - index > max_length:
                break
            if s[index : i + 1] not in WordDict:
                continue
            memo[index] += self.memo_search(s, i + 1, WordDict, max_length, memo)

        return memo[index]
      
