Description:
You are given an array of strings arr that represents a valid arithmetic expression written in Reverse Polish Notation (Postfix Notation). Your task is to evaluate the expression and return an integer representing its value.

Key Details:

The valid operators are '+', '-', '*', and '/'.
Each operand is guaranteed to be a valid integer or another expression.
The division operation between two integers always rounds the result towards zero, discarding any fractional part.
No division by zero will occur in the input.
The input is a valid arithmetic expression in Reverse Polish Notation.
The result of the expression and all intermediate calculations will fit in a 32-bit signed integer.
Examples:

Input: arr = ["2", "3", "1", "*", "+", "9", "-"]
Output: -4
Explanation: If the expression is converted into an infix expression, it will be 2 + (3 * 1) – 9 = 5 – 9 = -4.
Input: arr = ["100", "200", "+", "2", "/", "5", "*", "7", "+"]
Output: 757
Explanation: If the expression is converted into an infix expression, it will be ((100 + 200) / 2) * 5 + 7  = 150 * 5 + 7 = 757.
Constraints:

1 <= arr.size() <= 105
arr[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-104, 104]

Python3:
class Solution:
    def evaluate(self, arr):
        stack = []
        
        for token in arr:
            if token in "+-*/":
                # Pop the top two elements from the stack
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Handle division rounding towards zero
                    stack.append(int(a / b))  # Using int() to round towards zero
            else:
                # If the token is a number, push it onto the stack
                stack.append(int(token))
        
        # The result is the only element left in the stack
        return stack[0]

# Example usage:
solution = Solution()

# Test Case 1
arr1 = ["2", "3", "1", "*", "+", "9", "-"]
print(solution.evaluate(arr1))  # Output: -4

# Test Case 2
arr2 = ["100", "200", "+", "2", "/", "5", "*", "7", "+"]
print(solution.evaluate(arr2))  # Output: 757
