Description:
Given a binary tree and an integer k, determine the number of downward-only paths where the sum of the node values in the path equals k. A path can start and end at any node within the tree but must always move downward (from parent to child).

Examples:

Input: k = 7   

Output: 3
Explanation: The following paths sum to k 
 
Input: k = 3
   1
  /  \
2     3
Output: 2
Explanation:
Path 1 : 1 -> 2 (Sum = 3)
Path 2 : 3 (Sum = 3)
Constraints:


Python3:
class Solution:
    def sumK(self, root, k):
        from collections import defaultdict
        
        # HashMap to store prefix sums and their frequencies
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Base case: Sum of 0 has one occurrence
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the prefix sum
            current_sum += node.data
            
            # Check if there exists a previous prefix sum to form a valid path
            count = prefix_sum_count[current_sum - k]
            
            # Update the prefix sum count
            prefix_sum_count[current_sum] += 1
            
            # Recursively check left and right subtrees
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Backtrack (remove the current sum before returning to the parent)
            prefix_sum_count[current_sum] -= 1
            
            return count
        
        return dfs(root, 0)
