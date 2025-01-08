Description:
Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle. 

A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

Examples:

Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle.  
Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]
Input: arr[] = [1, 2, 3]
Output: 0
Explanation: No triangles are possible.
Constraints:
3 <= arr.size() <= 103
0 <= arr[i] <= 105
Python3:
class Solution:
    # Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # Sort the array to simplify the triangle condition check
        arr.sort()
        n = len(arr)
        count = 0
        
        # Fix the third side as arr[k] and find all valid pairs for i and j
        for k in range(n - 1, 1, -1):  # Start from the largest side
            i = 0
            j = k - 1
            while i < j:
                # Check if arr[i] + arr[j] > arr[k]
                if arr[i] + arr[j] > arr[k]:
                    # All pairs (i, j), (i+1, j), ..., (j-1, j) satisfy the condition
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        
        return count
