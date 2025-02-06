Description:
Given two arrays representing the inorder and preorder traversals of a binary tree, construct the tree and return the root node of the constructed tree.

Note: The output is written in postorder traversal.

Examples:

Input: inorder[] = [1, 6, 8, 7], preorder[] = [1, 6, 7, 8]
Output: [8, 7, 6, 1]
Explanation: The tree will look like

Input: inorder[] = [3, 1, 4, 0, 2, 5], preorder[] = [0, 1, 3, 4, 2, 5]
Output: [3, 4, 1, 5, 2, 0]
Explanation: The tree will look like

Input: inorder[] = [2, 5, 4, 1, 3], preorder[] = [1, 4, 5, 2, 3]
Output: [2, 5, 4, 3, 1]
Explanation: The tree will look like

Constraints:
1 ≤ number of nodes ≤ 103
0 ≤ nodes -> data ≤ 103
Both the inorder and preorder arrays contain unique values.


Python3:
# Definition for a binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        # Create a hashmap to store indexes of inorder elements for quick lookup
        inorder_map = {value: idx for idx, value in enumerate(inorder)}
        self.preorder_index = 0  # Track the current index in preorder traversal

        def constructTree(left, right):
            # Base case: If there are no elements to construct the tree
            if left > right:
                return None
            
            # Pick current node from preorder traversal using preorder_index
            root_value = preorder[self.preorder_index]
            self.preorder_index += 1
            root = Node(root_value)
            
            # Find the index of this node in inorder traversal
            inorder_index = inorder_map[root_value]
            
            # Recursively build left and right subtrees
            root.left = constructTree(left, inorder_index - 1)
            root.right = constructTree(inorder_index + 1, right)
            
            return root
        
        return constructTree(0, len(inorder) - 1)

    def postorderTraversal(self, root):
        result = []
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(node.data)
        postorder(root)
        return result
