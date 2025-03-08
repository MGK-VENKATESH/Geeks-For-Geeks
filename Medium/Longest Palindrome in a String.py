Description:
Given a string s, your task is to find the longest palindromic substring within s.

A substring is a contiguous sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).

A palindrome is a string that reads the same forward and backward. More formally, s is a palindrome if reverse(s) == s.

Note: If there are multiple palindromic substrings with the same length, return the first occurrence of the longest palindromic substring from left to right.

Examples :

Input: s = “forgeeksskeegfor” 
Output: “geeksskeeg”
Explanation: There are several possible palindromic substrings like “kssk”, “ss”, “eeksskee” etc. But the substring “geeksskeeg” is the longest among all.
Input: s = “Geeks” 
Output: “ee”
Explanation: "ee" is the longest palindromic substring of "Geeks". 
Input: s = “abc” 
Output: “a”
Explanation: "a", "b" and "c" are longest palindromic substrings of same length. So, the first occurrence is returned.
Constraints:
1 ≤ s.size() ≤ 103
s consist of only lowercase English letters.

Python3:
class Solution:
    def longestPalindrome(self, s):
        if not s or len(s) == 1:
            return s
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Extract the palindrome
        
        longest = ""
        
        for i in range(len(s)):
            # Check for odd-length palindromes (single character as center)
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # Check for even-length palindromes (two characters as center)
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest
