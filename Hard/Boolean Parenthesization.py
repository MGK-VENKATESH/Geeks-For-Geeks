Description:
You are given a boolean expression s containing
    'T' ---> true
    'F' ---> false 
and following operators between symbols
   &   ---> boolean AND
    |   ---> boolean OR
   ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Note: The answer is guaranteed to fit within a 32-bit integer.

Examples:

Input: s = "T|T&F^T"
Output: 4
Explaination: The expression evaluates to true in 4 ways: ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).
Input: s = "T^F|F"
Output: 2
Explaination: The expression evaluates to true in 2 ways: ((T^F)|F) and (T^(F|F)).
Constraints:
1 ≤ |s| ≤ 100 


Python3:
#User function Template for python3
class Solution:
    def countWays(self, expr):
        # code here
        n = len(expr)
        dp = [[[0]*2 for _ in range(n)] for _ in range(n)]
        
        for i in range(n-1, -1, -2):
            for j in range(i, n, 2):
                if i == j:
                    dp[i][j][0] = int(expr[i] == 'F')
                    dp[i][j][1] = int(expr[i] == 'T')
                else:
                    for k in range(i+1, j, 2):
                        match expr[k]:
                            case '&':
                                dp[i][j][1] += dp[i][k-1][1]*dp[k+1][j][1]
                                dp[i][j][0] += dp[i][k-1][0]*dp[k+1][j][0]
                                dp[i][j][0] += dp[i][k-1][1]*dp[k+1][j][0]
                                dp[i][j][0] += dp[i][k-1][0]*dp[k+1][j][1]
                            case '|':
                                dp[i][j][1] += dp[i][k-1][1] * dp[k+1][j][1]    
                                dp[i][j][1] += dp[i][k-1][0] * dp[k+1][j][1]
                                dp[i][j][1] += dp[i][k-1][1] * dp[k+1][j][0]
                                dp[i][j][0] += dp[i][k-1][0] * dp[k+1][j][0]
                            case '^':
                                dp[i][j][1] += dp[i][k-1][0] * dp[k+1][j][1] + dp[i][k-1][1] * dp[k+1][j][0]
                                dp[i][j][0] += dp[i][k-1][0] * dp[k+1][j][0] + dp[i][k-1][1] * dp[k+1][j][1]
        #print(dp)
        return dp[0][-1][1]
