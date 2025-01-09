Description:
Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.
Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.
Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 103
0 <= target <= 109

Python3:
class Solution:
    def subarraySum(self, arr, target):
        # Initialize pointers and variables
        left, current_sum = 0, 0
        
        # Traverse the array
        for right in range(len(arr)):
            # Add the current element to the current sum
            current_sum += arr[right]
            
            # While the current sum exceeds the target, move the left pointer
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
            
            # If the current sum equals the target, return the indices
            if current_sum == target:
                return [left + 1, right + 1]  # Convert 0-based to 1-based index
        
        # If no subarray is found, return [-1]
        return [-1]
