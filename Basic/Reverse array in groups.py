Description:
Given an array arr of positive integers. Reverse every sub-array group of size k.

Note: If at any instance, k is greater or equal to the array size, then reverse the entire array. You shouldn't return any array, modify the given array in place.

Examples:

Input: k = 3, arr= [1, 2, 3, 4, 5]
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
Input: k = 5, arr = [5, 6, 8, 9]
Output: [9, 8, 6, 5]
Explnation: Since k is greater than array size, the entire array is reversed.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size(), k ≤ 107
1 ≤ arr[i] ≤ 1018
Python3:
class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):
        n = len(arr)  # Calculate the size of the array
        for i in range(0, n, k):
            end = min(i + k, n)
            arr[i:end] = arr[i:end][::-1]
