Description:
Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing from arr[].  

Examples :

Input: arr[] = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: Missing are 1, 5, 6, 8, 9, 10… and 5th missing number is 9.
Input: arr[] = [1, 2, 3], k = 2
Output: 5
Explanation: Missing are 4, 5, 6… and 2nd missing number is 5.
Input: arr[] = [3, 5, 9, 10, 11, 12], k = 2
Output: 2
Explanation: Missing are 1, 2, 4, 6… and 2nd missing number is 2.
Constraints:
1 <= arr.size() <= 105
1 <= k <= 105
1 <= arr[i]<= 106
Python3:
class Solution:
    def kthMissing(self, arr, k):
        # Initialize the current missing count
        missing_count = 0
        # Initialize the current number we're looking for
        current_number = 1
        # Iterate through the array
        for num in arr:
            while current_number < num:
                missing_count += 1
                if missing_count == k:
                    return current_number
                current_number += 1
            current_number = num + 1  # Move to the next number after the current element in arr
        # If kth missing number is beyond the last element in arr
        while missing_count < k:
            missing_count += 1
            if missing_count == k:
                return current_number
            current_number += 1
