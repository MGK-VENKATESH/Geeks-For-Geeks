Description:
Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

Examples:

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.
Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.
Input: arr[] = [0]
Output: 0
Explnation: There is no subarray with an equal number of 0s and 1s.
Constraints:
1 <= arr.size() <= 105
0 <= arr[i] <= 1

Python3:
class Solution:
    def maxLen(self, arr):
        # Replace 0 with -1
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                arr[i] = -1
        
        # Initialize variables
        max_length = 0
        cumulative_sum = 0
        sum_indices = {0: -1}  # Store cumulative sum and first index
        
        # Traverse the array
        for i in range(n):
            cumulative_sum += arr[i]
            
            # If cumulative sum has been seen before
            if cumulative_sum in sum_indices:
                max_length = max(max_length, i - sum_indices[cumulative_sum])
            else:
                sum_indices[cumulative_sum] = i
        
        return max_length
