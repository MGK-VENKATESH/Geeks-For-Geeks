Description:
Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.

Note: The final output will be in lexicographic order.

Examples:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.
Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]
Explanation: 
Group 1: "abc", "bac", and "cab" are anagrams.
Group 2: "listen", "silent", and "enlist" are anagrams.
Group 3: "rat", "tar", and "art" are anagrams.
Constraints:
1<= arr.size() <=100
1<= arr[i].size() <=10

Python3:
class Solution:

    def anagrams(self, arr):
        # Dictionary to map sorted key to the group of anagrams
        anagram_map = {}
        order = []  # Keeps track of the order of the keys as they appear

        for word in arr:
            # Sort characters to form the key
            key = ''.join(sorted(word))
            if key not in anagram_map:
                anagram_map[key] = []
                order.append(key)  # Maintain the order of groups
            anagram_map[key].append(word)

        # Create result in the order of first appearance of keys
        result = [anagram_map[key] for key in order]
        
        return result
