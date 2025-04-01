Description:
Given an array, arr of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: 2 3 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.
Input: arr[] = [1, 1, 1]
Output: -1
Explanation: Only element is 1 which is smallest, so there is no second smallest element.
Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
1 <= arr.size <= 105
1 <= arr[i] <= 105


Python3:
from typing import List
class Solution:
    def minAnd2ndMin(self, arr):
        #code 
        arr.sort()
        smallest = arr[0]
        second_smallest = -1
        
        for num in arr[1:]:  # Find first number larger than smallest
            if num > smallest:
                second_smallest = num
                break
        
        return [smallest, second_smallest] if second_smallest != -1 else [-1]

        
