Description:
Given an array arr[] of positive integers and another integer target. Determine if there exists two distinct indices such that the sum of there elements is equals to target.

Examples:

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 16
Output: true
Explanation: arr[3] + arr[4] = 6 + 10 = 16.
Input: arr[] = [1, 2, 4, 3, 6], target = 11
Output: false
Explanation: None of the pair makes a sum of 11.
Constraints:
1 ≤ arr.size ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ target ≤ 2*105
Python3:
class Solution:
    def twoSum(self, arr, target):
        # Create a set to store visited numbers
        seen = set()

        # Traverse the array
        for num in arr:
            complement = target - num
            if complement in seen:
                return True  # If complement exists, return True
            seen.add(num)  # Add the current number to the set

        return False  # If no pair found, return False
