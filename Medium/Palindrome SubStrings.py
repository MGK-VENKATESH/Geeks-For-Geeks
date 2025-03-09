Description:
Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string must be greater than or equal to 2. 

Examples

Input: s = "abaab"
Output: 3
Explanation: All palindromic substrings are : "aba" , "aa" , "baab".
Input: s = "aaa"
Output: 3
Explanation: All palindromic substrings are : "aa", "aa", "aaa".
Input: s = "abbaeae"
Output: 4
Explanation: All palindromic substrings are : "bb" , "abba" , "aea", "eae".
Constraints:
2 ≤ s.size() ≤ 103
string contains only lowercase english characters


Python3:
class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0  # To store the count of palindromic substrings
        
        def expandAroundCenter(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= 2:  # Only count substrings of length >= 2
                    count += 1
                left -= 1
                right += 1
        
        for i in range(n):
            # Check for odd-length palindromes (single character as center)
            expandAroundCenter(i, i)

            # Check for even-length palindromes (two characters as center)
            expandAroundCenter(i, i + 1)
        
        return count
