Description:
Given a string str, your task is to find the length of the smallest window that contains all the characters of the given string at least once.

Example:

Input: str = "aabcbcdbca"
Output: 4
Explanation: Sub-String "dbca" has the smallest length that contains all the characters of str.
Input: str = "aaab"
Output: 2
Explanation: Sub-String "ab" has the smallest length that contains all the characters of str.
Input: str = "geeksforgeeks"
Output: 8
Explanation: There are multiple substring with smallest length that contains all characters of str, "geeksfor" and "forgeeks". 
Constraints:
1 ≤ str.size() ≤ 105
str contains only lower-case english alphabets.
class Solution:
    def findSubString(self, s):
        from collections import defaultdict

        n = len(s)
        if n == 0:
            return 0

        # Step 1: Get number of unique characters
        unique_chars = set(s)
        required_char_count = len(unique_chars)

        # Step 2: Initialize pointers and counts
        start = 0
        min_len = n + 1
        char_count = defaultdict(int)
        formed = 0

        for end in range(n):
            char_count[s[end]] += 1
            if char_count[s[end]] == 1:
                formed += 1

            # Try to shrink the window
            while formed == required_char_count:
                if end - start + 1 < min_len:
                    min_len = end - start + 1

                # Shrink from start
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    formed -= 1
                start += 1

        return min_len

Python3:
