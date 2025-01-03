Description:
Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

Examples

Input: root = [5, 4, 6, 3, N, N, 7, 1]
ex-1
Output: 1
Input: root = [10, 5, 20, 2]
ex-2
Output: 2
Input: root = [10, N, 10, N, 11]
             10
              \
               10
                \
                 11
Output: 10
Constraints:
0 <= number of nodes <= 105
0 <= node->data <= 105


Python3:
"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    # Function to find the minimum element in the given BST.
    def minValue(self, root):
        # Initialize a pointer to traverse the tree
        current = root
        
        # Traverse to the leftmost node
        while current and current.left:
            current = current.left
        
        # The current node now points to the minimum value node
        return current.data if current else None

