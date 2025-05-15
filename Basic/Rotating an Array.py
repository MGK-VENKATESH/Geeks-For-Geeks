Description:
Given an array arr[]. The task is to rotate the array by d elements where d ≤ arr.size.

Examples:

Input: arr[] = [-1, -2, -3, 4, 5, 6, 7], d = 2
Output: [-3, 4, 5, 6, 7, -1, -2]
Explanation: 
Rotate by 1: [-2, -3, 4, 5, 6, 7, -1]
Rotate by 2: [-3, 4, 5, 6, 7, -1, -2]
Input: arr[] = [1, 3, 4, 2], d = 3 
Output: [2, 1, 3, 4]
Explanation: After rotating the array three times, the first three elements shift one by one to the right.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size ≤ 106
-109 ≤ arr[i] ≤ 109
0 ≤ d ≤ arr.size


Python3:
class Solution:
    def leftRotate(self, arr, d):
        # code here
        n = len(arr)
        d = d % n
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        reverse(0, d - 1)
        reverse(d, n - 1)
        reverse(0, n - 1)
