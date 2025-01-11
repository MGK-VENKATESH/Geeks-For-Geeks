Description:
Given a string s, find the length of the longest substring with all distinct characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.
Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.
Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.
Constraints:
1<= s.size()<=3*104
All the characters are in lowercase.

Python3:
class Solution:
    def longestUniqueSubstr(self, s: str) -> int:
        # Initialize a set to track unique characters in the current window
        char_set = set()
        # Initialize pointers for the sliding window and the max length
        left = 0
        max_length = 0
        
        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If the character is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update the max length if needed
            max_length = max(max_length, right - left + 1)
        
        return max_length
