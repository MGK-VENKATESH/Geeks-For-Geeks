Description:
You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB. For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k = 1.

Return the length of the longest possible word chain with words chosen from the given list of words in any order.

Examples:

Input: words[] = ["ba", "b", "a", "bca", "bda", "bdca"]
Output: 4
Explanation: One of the longest word chains is ["a", "ba", "bda", "bdca"].
Input: words[] = ["abc", "a", "ab"]
Output: 3
Explanation: The longest chain is {"a", "ab" "abc"}
Input: words[] = ["abcd", "dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
Constraint:
1 <= words.length <= 104
1 <= words[i].length <= 10
 words[i] only consists of lowercase English letters.

Python3:
class Solution:
    def longestStringChain(self, words):
        words.sort(key=len)  # Sort words by length
        dp = {}  # Dictionary to store longest chain ending at each word
        max_chain = 1  # At least one word can be a chain itself

        for word in words:
            dp[word] = 1  # Initialize with chain length 1
            for i in range(len(word)):  # Try removing each character
                predecessor = word[:i] + word[i+1:]  # Create predecessor
                if predecessor in dp:  # If valid predecessor exists
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            max_chain = max(max_chain, dp[word])  # Update max chain length

        return max_chain  # Return the longest word chain length

# Example Usage:
solution = Solution()
words1 = ["ba", "b", "a", "bca", "bda", "bdca"]
print(solution.longestStringChain(words1))  # Output: 4

words2 = ["abc", "a", "ab"]
print(solution.longestStringChain(words2))  # Output: 3

words3 = ["abcd", "dbqca"]
print(solution.longestStringChain(words3))  # Output: 1


