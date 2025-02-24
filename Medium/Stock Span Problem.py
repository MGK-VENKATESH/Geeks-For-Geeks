Description:
The stock span problem is a financial problem where we have a series of daily price quotes for a stock and we need to calculate the span of stock price for all days. The span arr[i] of the stocks price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the given day is less than or equal to its price on the current day.

Examples:

Input: arr[] = [100, 80, 60, 70, 60, 75, 85]
Output: [1, 1, 1, 2, 1, 4, 6]
Explanation: Traversing the given input span 100 is greater than equal to 100 and there are no more elements behind it so the span is 1, 80 is greater than equal to 80 and smaller than 100 so the span is 1, 60 is greater than equal to 60 and smaller than 80 so the span is 1, 70 is greater than equal to 60,70 and smaller than 80 so the span is 2 and so on.  Hence the output will be 1 1 1 2 1 4 6.
Input: arr[] = [10, 4, 5, 90, 120, 80]
Output: [1, 1, 2, 4, 5, 1]
Explanation: Traversing the given input span 10 is greater than equal to 10 and there are no more elements behind it so the span is 1, 4 is greater than equal to 4 and smaller than 10 so the span is 1, 5 is greater than equal to 4,5 and smaller than 10 so the span is 2,  and so on. Hence the output will be 1 1 2 4 5 1.
Input: arr[] = [11, 4, 5, 90, 120, 80]
Output: [1, 1, 2, 4, 5, 1]
Explanation: Traversing the given input span 11 is greater than equal to 11 and there are no more elements behind it so the span is 1, 4 is greater than equal to 4 and smaller than 10 so the span is 1, 5 is greater than equal to 4,5 and smaller than 10 so the span is 2, and so on. Hence the output will be 1 1 2 4 5 1.
Constraints:
1 ≤ arr.size()≤ 105
1 ≤ arr[i] ≤ 105

Python3:
class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n  # Result array
        stack = []  # Stack to store indices

        for i in range(n):
            # Remove elements from stack while they are <= current price
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            # If stack is empty, span is entire length up to i
            span[i] = i + 1 if not stack else i - stack[-1]

            # Push current index to stack
            stack.append(i)

        return span

# Example usage
sol = Solution()
print(sol.calculateSpan([100, 80, 60, 70, 60, 75, 85]))  # Output: [1, 1, 1, 2, 1, 4, 6]
print(sol.calculateSpan([10, 4, 5, 90, 120, 80]))  # Output: [1, 1, 2, 4, 5, 1]
print(sol.calculateSpan([11, 4, 5, 90, 120, 80]))  # Output: [1, 1, 2, 4, 5, 1]
