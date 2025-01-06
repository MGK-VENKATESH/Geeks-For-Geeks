Description:
Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.
Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. 
Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.
Constraints:
1 <= arr.size() <= 2*105
0 <= target<= 2*105
0 <= arr[i] <= 105

Python3:
class Solution:
    def sumClosest(self, arr, target):
        # If array has less than 2 elements, return an empty list
        if len(arr) < 2:
            return []
        
        # Sort the array to use two-pointer approach
        arr.sort()
        left, right = 0, len(arr) - 1
        closest_sum = float('inf')
        result_pair = []

        while left < right:
            current_sum = arr[left] + arr[right]
            diff = abs(target - current_sum)

            # Check if this pair is closer to the target
            if diff < abs(target - closest_sum) or (diff == abs(target - closest_sum) and abs(arr[right] - arr[left]) > abs(result_pair[1] - result_pair[0] if result_pair else 0)):
                closest_sum = current_sum
                result_pair = [arr[left], arr[right]]

            # Move pointers based on current sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
        
        return result_pair
