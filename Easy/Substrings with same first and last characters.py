Description:
Given a string s consisting of lowercase characters, the task is to find the count of all substrings that start and end with the same character.

Examples:

Input: s = "abcab"
Output: 7
Explanation: There are 7 substrings where the first and last characters are the same: "a", "abca", "b", "bcab", "c", "a", and "b"
Input: s = "aba"
Output: 4
Explanation: There are 4 substrings where the first and last characters are the same: "a", "aba", "b", "a"
Constraints:
1 <= |s| <= 104
s contains lower case english alphabets


Python3:
from collections import Counter
class Solution:
	def countSubstring(self, s):
		# code here
		freq = Counter(s)
		count = 0
		for c in freq:
		    f = freq[c]
		    count += f * (f - 1) // 2
		    count += f
		return count
