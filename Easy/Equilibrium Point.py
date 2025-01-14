Description:
Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 0 + 3 = 3.
Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.
Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.
Constraints:
3 <= arr.size() <= 106
-109 <= arr[i] <= 109

Python3:
class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)  # Compute total sum of the array
        left_sum = 0          # Initialize left sum as 0
        
        for i in range(len(arr)):
            # Update right sum by subtracting the current element
            total_sum -= arr[i]
            
            # Check if left sum equals right sum
            if left_sum == total_sum:
                return i  # Return the index
            
            # Update left sum for the next iteration
            left_sum += arr[i]
        
        return -1  # If no equilibrium point is found
