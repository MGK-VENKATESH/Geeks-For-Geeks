Description:
Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

Examples: 

Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.
Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.
 
Input: arr[] = [1, 1, 1, 1], k = 0
Output: 4
Explanation: The subarrays are [1, 1], [1, 1], [1, 1] and [1, 1, 1, 1] 
 

Constraints:

1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤105
0 ≤ k ≤ 105

Python3:
class Solution:
    def subarrayXor(self, arr, k):
        # Dictionary to store the frequency of cumulative XORs
        xor_count = {}
        xor = 0  # Initialize cumulative XOR
        count = 0  # Initialize count of subarrays

        for num in arr:
            # Update the cumulative XOR
            xor ^= num

            # If cumulative XOR is equal to k, it means the subarray from the start has XOR k
            if xor == k:
                count += 1

            # Check if there's a prefix XOR such that (prefix XOR ^ k) == current XOR
            if xor ^ k in xor_count:
                count += xor_count[xor ^ k]

            # Add the current XOR to the hashmap
            xor_count[xor] = xor_count.get(xor, 0) + 1

        return count
