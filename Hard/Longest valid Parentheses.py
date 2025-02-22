Description:
Given a string s consisting of opening and closing parenthesis '(' and ')'. Find the length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
The closing parenthesis must be after its opening parenthesis.
Examples :

Input: s = "((()"
Output: 2
Explanation: The longest valid parenthesis substring is "()".
Input: s = ")()())"
Output: 4
Explanation: The longest valid parenthesis substring is "()()".
Input: s = "())()"
Output: 2
Explanation: The longest valid parenthesis substring is "()".
Constraints:
1 ≤ s.size() ≤ 106  
s consists of '(' and ')' only
Python3:

class Solution:
    def maxLength(self, s):
        # code here
        n = len(s)
        left = right = max_length = 0
    
        # Left to right scan
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                left = right = 0
    
        # Reset counters for right to left scan
        left = right = 0
    
        # Right to left scan
        for i in range(n-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
    
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0
    
        return max_length
                                                                                                                                       
                 
            
