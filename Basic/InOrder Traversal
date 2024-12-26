Description:
Given a Binary Tree, find the In-Order Traversal of it.

Examples:

Input:
       1
     /  \
    3    2
Output: [3, 1, 2]
Explanation: The in-order traversal of the given binary tree is [3, 1, 2].
Input:
        10
     /      \ 
    20       30 
  /    \    /
 40    60  50
Output: [40, 20, 60, 10, 50, 30]
Explanation: The in-order traversal of the given binary tree is [40, 20, 60, 10, 50, 30].
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= number of nodes <= 105
0 <= node->data <= 105

Python3:
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        # code here
        if root is None:
            return []
        result = []
        result.extend(self.InOrder(root.left))
        result.append(root.data)
        result.extend(self.InOrder(root.right))
        
        return result
