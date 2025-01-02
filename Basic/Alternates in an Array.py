Description:
You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 1 3
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4
Input: arr[] = [1, 2, 3, 4, 5]
Output: 1 3 5
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4
Take fifth element: 5
Constraints:
1 <=  arr.size <= 105
1 <= arr[i] <= 105

Python3:
#User function Template for python3
class Solution:
    def getAlternates(self, arr):
        # Code Here
        return arr[::2]
