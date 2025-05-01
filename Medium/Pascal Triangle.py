Description:
Given a positive integer n, return the nth row of pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of previous row.

File:PascalTriangleAnimated2.gif

Examples:

Input: n = 4
Output: [1, 3, 3, 1]
Explanation: 4th row of pascal's triangle is [1, 3, 3, 1].
Input: n = 5
Output: [1, 4, 6, 4, 1]
Explanation: 5th row of pascal's triangle is [1, 4, 6, 4, 1].
Input: n = 1
Output: [1]
Explanation: 1st row of pascal's triangle is [1].
Constraints:
1 ≤ n ≤ 20


Python3:
class Solution:
    def nthRowOfPascalTriangle(self, n):
        row = [1]
        prev = 1
        for i in range(1, n):
            # Use the relationship: C(n, k) = C(n, k-1) * (n - k) / k
            curr = (prev * (n - i)) // i
            row.append(curr)
            prev = curr
        return row
