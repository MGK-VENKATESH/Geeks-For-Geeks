Description:
Given a string s of lowercase English alphabets, your task is to return the maximum number of substrings formed, after possible partitions (probably zero) of s such that no two substrings have a common character.

Examples:

Input: s = "acbbcc"
Output: 2
Explanation: "a" and "cbbcc" are two substrings that do not share any characters between them.
Input: s = "ababcbacadefegdehijhklij"
Output: 3
Explanation: Partitioning at the index 8 and at 15 produces three substrings: “ababcbaca”, “defegde”, and “hijhklij” such that none of them have a common character. So, the maximum number of substrings formed is 3.
Input: s = "aaa"
Output: 1
Explanation: Since the string consists of same characters, no further partition can be performed. Hence, the number of substring (here the whole string is considered as the substring) is 1.
Constraints:
1 ≤ s.size() ≤ 105
'a' ≤ s[i] ≤ 'z' 

Python3:
class Solution:
    def maxPartitions(self, s: str) -> int:
        # Step 1: Store the last occurrence of each character
        last_occurrence = {ch: i for i, ch in enumerate(s)}
        
        partitions = 0
        max_last = 0
        start = 0
        
        # Step 2: Iterate through the string
        for i, ch in enumerate(s):
            max_last = max(max_last, last_occurrence[ch])
            
            # If the current index reaches the max_last, we found a partition
            if i == max_last:
                partitions += 1
                start = i + 1  # Move start to the next index
        
        return partitions
