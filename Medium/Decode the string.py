Description:
Given an encoded string s, the task is to decode it. The encoding rule is :

k[encodedString], where the encodedString inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
Note: The test cases are generated so that the length of the output string will never exceed 105 .

Examples:

Input: s = "1[b]"
Output: "b"
Explanation: "b" is present only one time.
Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation:
1. Inner substring “2[ca]” breakdown into “caca”.
2. Now, new string becomes “3[bcaca]”
3. Similarly “3[bcaca]” becomes “bcacabcacabcaca ” which is final result.
Constraints:
1 ≤ |s| ≤ 105 

Python3:
class Solution:
    def decodedString(self, s):
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                # Extract the encoded string inside []
                decoded_str = ""
                while stack and stack[-1] != "[":
                    decoded_str = stack.pop() + decoded_str  # Build the string in correct order
                
                stack.pop()  # Remove '['
                
                # Extract the number (k) before '['
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num  # Build number from right to left
                
                k = int(num)  # Convert to integer
                
                # Repeat the decoded string k times and push back to stack
                stack.append(decoded_str * k)
        
        return "".join(stack)  # Combine everything in the stack

# Example Usage:
solution = Solution()

# Test Case 1
s1 = "1[b]"
print(solution.decodedString(s1))  # Output: "b"

# Test Case 2
s2 = "3[b2[ca]]"
print(solution.decodedString(s2))  # Output: "bcacabcacabcaca"

# Test Case 3
s3 = "2[a2[b]]"
print(solution.decodedString(s3))  # Output: "abbabb"
