Description:
Given two strings s1 and s2. Return the minimum number of operations required to convert s1 to s2.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.
Examples:

Input: s1 = "geek", s2 = "gesek"
Output: 1
Explanation: One operation is required, inserting 's' between two 'e' in s1.
Input: s1 = "gfg", s2 = "gfg"
Output: 0
Explanation: Both strings are same.
Input: s1 = "abcd", s2 = "bcfe"
Output: 3
Explanation: We can convert s1 into s2 by removing ‘a’, replacing ‘d’ with ‘f’ and inserting ‘e’ at the end. 
Constraints:
1 ≤ s1.length(), s2.length() ≤ 103
Both the strings are in lowercase.


Python3:
class Solution:
    def editDistance(self, s1, s2):
        # Code here
        n1=len(s1)
        n2=len(s2)
        dp = [[float("inf")]*(len(s2)+1) for _ in range(len(s1)+1)]
        
        for j in range(n2+1):
            dp[n1][j] = n2-j
        
        for i in range(n1+1):
            dp[i][n2] = n1-i
            
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                if s1[i]==s2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
         
        return dp[0][0]
