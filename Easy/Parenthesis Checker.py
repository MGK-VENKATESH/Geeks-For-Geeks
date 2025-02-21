Description:
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.

Examples :

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "([]"
Output: False
Explanation: The expression is not balanced as there is a missing ')' at the end.
Input: s = "([{]})"
Output: False
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.
Constraints:
1 ≤ s.size() ≤ 106
Python3:
class Solution:
    def isBalanced(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket, push to stack
                stack.append(char)
            elif char in bracket_map:  # If it's a closing bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False  # Mismatch found or stack is empty

        return len(stack) == 0  # Stack must be empty for a balanced expression

# Example usage
sol = Solution()
print(sol.isBalanced("[{()}]"))   # Output: True
print(sol.isBalanced("[()()]{}")) # Output: True
print(sol.isBalanced("([]"))      # Output: False
print(sol.isBalanced("([{]})"))   # Output: False
