Description:
Given a data stream arr[] where integers are read sequentially, the task is to determine the median of the elements encountered so far after each new integer is read.

There are two cases for median on the basis of data set size.

1. If the data set has an odd number then the middle one will be consider as median.
2. If the data set has an even number then there is no distinct middle value and the median will be the arithmetic mean of the two middle values.

Examples:

Input:  arr[] = [5, 15, 1, 3, 2, 8]
Output: [5.0, 10.0, 5.0, 4.0, 3.0, 4.0] 
Explanation: 
After reading 1st element of stream – 5 -> median = 5.0
After reading 2nd element of stream – 5, 15 -> median = (5+15)/2 = 10.0 
After reading 3rd element of stream – 5, 15, 1 -> median = 5.0
After reading 4th element of stream – 5, 15, 1, 3 ->  median = (3+5)/2 = 4.0
After reading 5th element of stream – 5, 15, 1, 3, 2 -> median = 3.0
After reading 6th element of stream – 5, 15, 1, 3, 2, 8 ->  median = (3+5)/2 = 4.0
Input: arr[] = [2, 2, 2, 2]
Output: [2.0, 2.0, 2.0, 2.0]
Explanation: 
After reading 1st element of stream – 2 -> median = 2.0
After reading 2nd element of stream – 2, 2 -> median = (2+2)/2 = 2.0
After reading 3rd element of stream – 2, 2, 2 -> median = 2.0
After reading 4th element of stream – 2, 2, 2, 2 ->  median = (2+2)/2 = 2.0
Constraints:
1 <= arr.size() <= 105
1 <= x <= 106

Python3:
import heapq

class Solution:
    def getMedian(self, arr):
        left = []  # Max-Heap (invert sign to use heapq as max-heap)
        right = []  # Min-Heap
        medians = []

        for num in arr:
            # Step 1: Insert into correct heap
            if not left or num <= -left[0]:
                heapq.heappush(left, -num)  # Store negative for max-heap behavior
            else:
                heapq.heappush(right, num)

            # Step 2: Balance the heaps
            if len(left) > len(right) + 1:
                heapq.heappush(right, -heapq.heappop(left))
            elif len(right) > len(left):
                heapq.heappush(left, -heapq.heappop(right))

            # Step 3: Compute median
            if len(left) > len(right):
                medians.append(float(-left[0]))  # Max-Heap root
            else:
                medians.append(((-left[0] + right[0]) / 2.0))  # Average of two middle elements

        return medians

# Example usage
arr1 = [5, 15, 1, 3, 2, 8]
arr2 = [2, 2, 2, 2]

sol = Solution()
print(sol.getMedian(arr1))  # Output: [5.0, 10.0, 5.0, 4.0, 3.0, 4.0]
print(sol.getMedian(arr2))  # Output: [2.0, 2.0, 2.0, 2.0]
