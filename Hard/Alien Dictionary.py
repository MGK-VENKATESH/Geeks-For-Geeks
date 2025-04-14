Description:
A new alien language uses the English alphabet, but the order of letters is unknown. You are given a list of words[] from the alien language’s dictionary, where the words are claimed to be sorted lexicographically according to the language’s rules.

Your task is to determine the correct order of letters in this alien language based on the given words. If the order is valid, return a string containing the unique letters in lexicographically increasing order as per the new language's rules. If there are multiple valid orders, return any one of them.

However, if the given arrangement of words is inconsistent with any possible letter ordering, return an empty string ("").

A string a is lexicographically smaller than a string b if, at the first position where they differ, the character in a appears earlier in the alien language than the corresponding character in b. If all characters in the shorter word match the beginning of the longer word, the shorter word is considered smaller.

Note: Your implementation will be tested using a driver code. It will print true if your returned order correctly follows the alien language’s lexicographic rules; otherwise, it will print false.

Examples:

Input: words[] = ["baa", "abcd", "abca", "cab", "cad"]
Output: true
Explanation: A possible corrct order of letters in the alien dictionary is "bdac".
The pair "baa" and "abcd" suggests 'b' appears before 'a' in the alien dictionary.
The pair "abcd" and "abca" suggests 'd' appears before 'a' in the alien dictionary.
The pair "abca" and "cab" suggests 'a' appears before 'c' in the alien dictionary.
The pair "cab" and "cad" suggests 'b' appears before 'd' in the alien dictionary.
So, 'b' → 'd' → 'a' → 'c' is a valid ordering.
Input: words[] = ["caa", "aaa", "aab"]
Output: true
Explanation: A possible corrct order of letters in the alien dictionary is "cab".
The pair "caa" and "aaa" suggests 'c' appears before 'a'.
The pair "aaa" and "aab" suggests 'a' appear before 'b' in the alien dictionary. 
So, 'c' → 'a' → 'b' is a valid ordering.
Input: words[] = ["ab", "cd", "ef", "ad"]
Output: ""
Explanation: No valid ordering of letters is possible.
The pair "ab" and "ef" suggests "a" appears before "e".
The pair "ef" and "ad" suggests "e" appears before "a", which contradicts the ordering rules.
Constraints:
1 ≤ words.length ≤ 500
1 ≤ words[i].length ≤ 100
words[i] consists only of lowercase English letters.
Python3:
#User function Template for python3
class Solution:
    def findOrder(words):
        # code here
        from collections import defaultdict
        from itertools import product
        
        g = defaultdict(set)
        n = len(words)
        chars = set(words[-1])
        for i in range(n-1):
            chars.update(words[i])
            for j in range(i+1, n):
                w1, w2 = words[i], words[j]
                for k in range(min(len(w1), len(w2))):
                    if w1[k] != w2[k]:
                        g[w1[k]].add(w2[k])
                        break
                else:
                    if len(w1) > len(w2):
                        return ""
                
        
        visited, on_stack = set(), set()
        result = []
        
        def dfs(n):
            if n in on_stack:
                return True 
            if n in visited:
                return False
            
            on_stack.add(n)
            for nbr in g.get(n, []):
                if dfs(nbr):
                    return True
            on_stack.remove(n)
            visited.add(n)
            result.append(n)
            
        for n in g.keys():
            if n not in visited:
                if dfs(n):
                    return ""
 
        result.extend(chars - set(result))
        return "".join(reversed(result))
