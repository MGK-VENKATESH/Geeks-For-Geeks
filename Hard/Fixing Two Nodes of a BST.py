Desscription:
Given the root of a Binary search tree(BST), where exactly two nodes were swapped by mistake. Your task is to fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Note: It is guaranteed that the given input will form BST, except for 2 nodes that will be wrong. All changes must be reflected in the original Binary search tree(BST).
 
Examples :
Input: root = [10, 5, 8, 2, 20]
     
Output: 1
       

Explanation: The nodes 20 and 8 were swapped. 
Input: root = [5, 10, 20, 2, 8]
     
Output: 1 
     
Explanation: The nodes 10 and 5 were swapped.
Constraints:
1 ≤ Number of nodes ≤ 103

Python3:
class Solution:
    def correctBST(self, root):
        # Initialize variables to track misplaced nodes
        self.first = self.middle = self.last = None
        self.prev = Node(float('-inf'))  # Previous node in inorder traversal
        
        # Function to perform inorder traversal and find misplaced nodes
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # Detect swapped nodes
            if self.prev and self.prev.data > node.data:
                if not self.first:  # First occurrence
                    self.first = self.prev
                    self.middle = node  # Might be adjacent
                else:  # Second occurrence
                    self.last = node
            
            self.prev = node  # Move to next node
            
            inorder(node.right)
        
        # Step 1: Identify misplaced nodes
        inorder(root)
        
        # Step 2: Swap the values of misplaced nodes
        if self.first and self.last:  # Non-adjacent swapped nodes
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:  # Adjacent swapped nodes
            self.first.data, self.middle.data = self.middle.data, self.first.data

        return 1  # Indicating that BST has been corrected
