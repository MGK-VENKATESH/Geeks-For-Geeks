Description:
Given an array of integers arr[], the task is to find the maximum of the minimum values for every possible window size in the array, where the window size ranges from 1 to arr.size().

More formally, for each window size k, determine the smallest element in all windows of size k, and then find the largest value among these minimums where 1<=k<=arr.size().

Examples :

Input: arr[] = [10, 20, 30, 50, 10, 70, 30]
Output: [70, 30, 20, 10, 10, 10, 10] 
Explanation: 
1. First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are [10], [20], [30], [50], [10], [70] and [30]. Maximum of these minimums is 70. 
2. Second element in output indicates maximum of minimums of all windows of size 2. Minimums of windows of size 2 are [10], [20], [30], [10], [10], and [30]. Maximum of these minimums is 30. 
3. Third element in output indicates maximum of minimums of all windows of size 3. Minimums of windows of size 3 are [10], [20], [10], [10] and [10]. Maximum of these minimums is 20. 
Similarly other elements of output are computed.
Input: arr[] = [10, 20, 30]
Output: [30, 20, 10]
Explanation: First element in output indicates maximum of minimums of all windows of size 1. Minimums of windows of size 1 are [10] , [20] , [30]. Maximum of these minimums are 30 and similarly other outputs can be computed
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 106


Python3:

class Solution:
    def maxOfMins(self, arr):
       # code here
       n = len(arr)
       nxs = self.next_smaller(arr)
       pvs = self.previous_smaller(arr)
       result = [float('-inf')]*n
    
       for i in range(n):
           idx = nxs[i] - pvs[i] - 2
           result[idx] = max(result[idx], arr[i])
           
       stack = []
       
       for i in reversed(range(n)):
           
           while stack and result[stack[-1]] < result[i]:
               stack.pop()
           
           if stack: result[i] = max(result[i], result[stack[-1]])
           stack.append(i)
           
       return result
       
    def next_smaller(self, arr):
        n = len(arr)
        nxs = [n]*n
        stack = []
        
        for i in reversed(range(n)):
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack: nxs[i] = stack[-1]
            stack.append(i)
        
        return nxs
    
    def previous_smaller(self, arr):
        n = len(arr)
        pxs = [-1]*n
        stack = []
        
        for i in range(n):
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack: pxs[i] = stack[-1]
            stack.append(i)
        
        return pxs
