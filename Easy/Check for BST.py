Description:
Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Examples:

Input: root = [2, 1, 3, N, N, N, 5]


Output: true 
Explanation: The left subtree of every node contains smaller keys and right subtree of every node contains greater keys. Hence, the tree is a BST.
Input: root = [2, N, 7, N, 6, N, 9] 



Output: false 
Explanation: Since the node to the right of node with key 7 has lesser key value, hence it is not a valid BST.
Input: root = [10, 5, 20, N, N, 9, 25]


Output: false
Explanation: The node with key 9 present in the right subtree has lesser key value than root node.
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 109

Python3:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isBSTUtil(self, root, min_val, max_val):
        if not root:
            return True
        
        # Check if the current node's value is within the valid range
        if not (min_val < root.data < max_val):
            return False
        
        # Recursively check left and right subtrees
        return (self.isBSTUtil(root.left, min_val, root.data) and
                self.isBSTUtil(root.right, root.data, max_val))

    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        return self.isBSTUtil(root, float('-inf'), float('inf'))
