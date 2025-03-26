Description:
You are given a string s and a list dictionary[] of words. Your task is to determine whether the string s can be formed by concatenating one or more words from the dictionary[].

Note: From dictionary[], any word can be taken any number of times and in any order.

Examples :

Input: s = "ilike", dictionary[] = ["i", "like", "gfg"]
Output: true
Explanation: s can be breakdown as "i like".
Input: s = "ilikegfg", dictionary[] = ["i", "like", "man", "india", "gfg"]
Output: true
Explanation: s can be breakdown as "i like gfg".
Input: s = "ilikemangoes", dictionary[] = ["i", "like", "man", "india", "gfg"]
Output: false
Explanation: s cannot be formed using dictionary[] words.
Constraints:
1 ≤ s.size() ≤ 3000
1 ≤ dictionary.size() ≤ 1000
1 ≤ dictionary[i].size() ≤ 100

Python3:
class Solution:
    def wordBreak(self, s, dictionary):
        d = set(dictionary)
        m = max((len(w) for w in dictionary), default=0)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if not dp[i]:
                continue
            for j in range(1, m + 1):
                if i + j <= n and s[i:i + j] in d:
                    dp[i + j] = True
        return dp[n]
