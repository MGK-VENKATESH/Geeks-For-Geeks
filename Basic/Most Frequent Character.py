Description:
Given a string s of lowercase alphabets. The task is to find the maximum occurring character in the string s. If more than one character occurs the maximum number of times then print the lexicographically smaller character.

Examples:

Input: s = "testsample"
Output: 'e'
Explanation: e is the character which is having the highest frequency.
Input: s = "output"
Output: 't'
Explanation:  t and u are the characters with the same frequency, but t is lexicographically smaller.
Constraints:
1 ≤ |s| ≤ 100

Python3:
class Solution:
    def getMaxOccurringChar(self, s):
        freq = [0] * 26  # Frequency of 'a' to 'z'
        
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        max_freq = 0
        max_char = ''
        
        for i in range(26):
            if freq[i] > max_freq:
                max_freq = freq[i]
                max_char = chr(i + ord('a'))
        
        return max_char
