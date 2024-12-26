Description:
Given a binary tree, find its preorder traversal.

Examples:

Input:
        1      
      /          
    4    
  /    \   
4       2
Output: [1, 4, 4, 2]
Input:
       6
     /   \
    3     2
     \   / 
      1 2
Output: [6, 3, 1, 2, 2] 
Input:
         8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
Output: [8, 3, 1, 6, 4, 7, 10, 14, 13]
Constraints:
1 <= number of nodes <= 105
0 <= node->data <= 106

Python3:
class Solution:
#Function to return a list containing the preorder traversal of the tree.
    
   
    # code here
    def preorder(self, root):
        # Base case: if the root is None, return an empty list
        if root is None:
            return []
        
        # Preorder traversal: root -> left -> right
        result = []
        result.append(root.data)  # Visit the root
        result.extend(self.preorder(root.left))  # Traverse left subtree
        result.extend(self.preorder(root.right))  # Traverse right subtree
        
        return result
