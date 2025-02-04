Description:
Given a binary tree, the diameter (also known as the width) is defined as the number of edges on the longest path between two leaf nodes in the tree. This path may or may not pass through the root. Your task is to find the diameter of the tree.

Examples:

Input: root[] = [1, 2, 3]

Output: 2
Explanation: The longest path has 2 edges (node 2 -> node 1 -> node 3).

Input: root[] = [5, 8, 6, 3, 7, 9]

Output: 4
Explanation: The longest path has 4 edges (node 3 -> node 8 -> node 5 -> node 6 -> node 9).

Constraints:
1 ≤ number of nodes ≤ 105
0 ≤ node->data ≤ 105

Python3:
class Solution:
    def diameter(self, root):
        self.max_diameter = 0  # Stores the maximum diameter found
        
        def height(node):
            if not node:
                return 0
            
            # Compute the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update max diameter (longest path in terms of edges)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of this node
            return 1 + max(left_height, right_height)
        
        height(root)  # Start DFS traversal from the root
        return self.max_diameter  # Return the maximum diameter found
