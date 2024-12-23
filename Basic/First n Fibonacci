Description:
Given a number n, return a list containing the first n Fibonacci numbers.

Note: The first two number of the series are 1 and 1.

Examples:

Input: n = 5
Output: [1, 1, 2, 3, 5]
Input: n = 7
Output: [1, 1, 2, 3, 5, 8, 13]
Input: n = 2
Output: [1, 1]
Constraints:
1<= n <=84
Python3:
class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        
        # your code here
        if n == 0:
            return []
        if n == 1:
            return [1]
        fib = [1,1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib
