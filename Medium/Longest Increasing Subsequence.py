Description:
Given an array arr[] of non-negative integers, the task is to find the length of the Longest Strictly Increasing Subsequence (LIS).

A subsequence is strictly increasing if each element in the subsequence is strictly less than the next element.

Examples:

Input: arr[] = [5, 8, 3, 7, 9, 1]
Output: 3
Explanation: The longest strictly increasing subsequence could be [5, 7, 9], which has a length of 3.
Input: arr[] = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output: 6
Explanation: One of the possible longest strictly increasing subsequences is [0, 2, 6, 9, 13, 15], which has a length of 6.
Input: arr[] = [3, 10, 2, 1, 20]
Output: 3
Explanation: The longest strictly increasing subsequence could be [3, 10, 20], which has a length of 3.
Constraints:
1 ≤ arr.size() ≤ 103
0 ≤ arr[i] ≤ 106
Python3:
from bisect import bisect_left

class Solution:
    def lis(self, arr):
        if not arr:
            return 0
        
        lis = []  # Stores the increasing sequence

        for num in arr:
            idx = bisect_left(lis, num)  # Find index to replace
            if idx == len(lis):
                lis.append(num)  # Extend the sequence
            else:
                lis[idx] = num  # Replace element (to keep LIS smallest)

        return len(lis)  # Length of LIS

# Example Usage:
solution = Solution()
arr1 = [5, 8, 3, 7, 9, 1]
print(solution.lis(arr1))  # Output: 3

arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(solution.lis(arr2))  # Output: 6

arr3 = [3, 10, 2, 1, 20]
print(solution.lis(arr3))  # Output: 3

