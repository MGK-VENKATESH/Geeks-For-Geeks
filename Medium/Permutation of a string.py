Description:
Given a string s, which may contain duplicate characters, your task is to generate and return an array of all unique permutations of the string. You can return your answer in any order.

Examples:

Input: s = "ABC"
Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
Explanation: Given string ABC has 6 unique permutations.
Input: s = "ABSG"
Output: ["ABGS", "ABSG", "AGBS", "AGSB", "ASBG", "ASGB", "BAGS", "BASG", "BGAS", "BGSA", "BSAG", "BSGA", "GABS", "GASB", "GBAS", "GBSA", "GSAB", "GSBA", "SABG", "SAGB", "SBAG", "SBGA", "SGAB", "SGBA"]
Explanation: Given string ABSG has 24 unique permutations.
Input: s = "AAA"
Output: ["AAA"]
Explanation: No other unique permutations can be formed as all the characters are same.
Constraints:
1 <= s.size() <= 9
s contains only Uppercase english alphabets

Python3:
class Solution:
    def findPermutation(self, s):
        def backtrack(path, used):
            # If the path length equals the length of the input string, add to result
            if len(path) == len(s):
                result.append("".join(path))
                return
            
            for i in range(len(s)):
                # Skip used characters or duplicate characters
                if used[i] or (i > 0 and s[i] == s[i - 1] and not used[i - 1]):
                    continue
                
                # Mark the character as used and backtrack
                used[i] = True
                path.append(s[i])
                backtrack(path, used)
                # Backtrack: remove the character and unmark it
                path.pop()
                used[i] = False

        # Sort the string to handle duplicates
        s = sorted(s)
        result = []
        used = [False] * len(s)
        backtrack([], used)
        return result
