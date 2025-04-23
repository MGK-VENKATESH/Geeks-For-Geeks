Description:
Given an array arr[] containing 2*n + 2 positive numbers, out of which 2*n numbers exist in pairs whereas the other two number occur exactly once and are distinct. Find the other two numbers. Return the answer in increasing order.

Examples:

Input: arr[] = [1, 2, 3, 2, 1, 4]
Output: [3, 4] 
Explanation: 3 and 4 occur exactly once.
Input: arr[] = [2, 1, 3, 2]
Output: [1, 3]
Explanation: 1 and 3 occur exactly once.
Input: arr[] = [2, 1, 3, 3]
Output: [1, 2]
Explanation: 1 and 2 occur exactly once.
Constraints:
2 ≤ arr.size() ≤ 106 
1 ≤ arr[i] ≤ 5 * 106
arr.size() is even


Python3:
class Solution:
    def singleNum(self, arr):
        xor = 0
        for num in arr:
            xor ^= num  # XOR of all elements
        
        # Get the rightmost set bit (i.e., bit where the two unique numbers differ)
        diff_bit = xor & -xor

        num1, num2 = 0, 0
        for num in arr:
            if num & diff_bit:
                num1 ^= num  # First group (bit is set)
            else:
                num2 ^= num  # Second group (bit is not set)
        
        return sorted([num1, num2])
