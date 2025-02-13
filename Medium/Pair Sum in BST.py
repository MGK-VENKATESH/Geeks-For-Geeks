Description:
Given a Binary Search Tree(BST) and a target. Check whether there's a pair of Nodes in the BST with value summing up to the target. 

Examples:

Input: root = [7, 3, 8, 2, 4, N, 9], target = 12
       bst
Output: True
Explanation: In the binary tree above, there are two nodes (8 and 4) that add up to 12.
Input: root = [9, 5, 10, 2, 6, N, 12], target = 23
          bst-3
Output: False
Explanation: In the binary tree above, there are no such two nodes exists that add up to 23.
Constraints:

1 ≤ Number of Nodes ≤ 105
1 ≤ target ≤ 106


Python3:
class Solution:
    def findTarget(self, root, target): 
        # Step 1: Perform inorder traversal to get sorted elements
        def inorder(node, elements):
            if not node:
                return
            inorder(node.left, elements)
            elements.append(node.data)
            inorder(node.right, elements)
        
        elements = []
        inorder(root, elements)  # Get sorted list
        
        # Step 2: Use two-pointer technique
        left, right = 0, len(elements) - 1
        while left < right:
            curr_sum = elements[left] + elements[right]
            if curr_sum == target:
                return True
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        
        return False
