Description:
Given a binary tree, the task is to find the maximum path sum. The path may start and end at any node in the tree.

Examples:

Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
Output: 42
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Input: root[] = [-17, 11, 4, 20, -2, 10]
Output: 31
Explanation: 

Max path sum is represented using green colour nodes in the above binary tree.
Constraints:
1 ≤ number of nodes ≤ 103
-104 ≤ node->data ≤ 104

Python3:
class Solution:
    def findMaxSum(self, root): 
        # Global variable to store the max sum
        self.max_sum = float('-inf')
        
        # Helper function to compute max path sum
        def maxPathSum(node):
            if not node:
                return 0
            
            # Compute the max path sum for left and right subtrees
            left = max(0, maxPathSum(node.left))  # Ignore negative sums
            right = max(0, maxPathSum(node.right))

            # Compute the maximum path sum including both children
            current_max = node.data + left + right

            # Update the global max sum if needed
            self.max_sum = max(self.max_sum, current_max)

            # Return the max sum **including only one subtree**
            return node.data + max(left, right)

        maxPathSum(root)
        return self.max_sum
