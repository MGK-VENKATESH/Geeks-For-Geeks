Description:
You are given a binary tree, and the task is to determine whether it satisfies the properties of a max-heap.

A binary tree is considered a max-heap if it satisfies the following conditions:

Completeness: Every level of the tree, except possibly the last, is completely filled, and all nodes are as far left as possible.
Max-Heap Property: The value of each node is greater than or equal to the values of its children.
Examples:

Input: root[] = [97, 46, 37, 12, 3, 7, 31, 6, 9]
 
Output: true
Explanation: The tree is complete and satisfies the max-heap property.
Input: root[] = [97, 46, 37, 12, 3, 7, 31, N, 2, 4] 
 
Output: false
Explanation: The tree is not complete and does not follow the Max-Heap Property, hence it is not a max-heap.
Constraints:
1 ≤ number of nodes ≤ 103
1 ≤ node->data ≤ 103


Python3:
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def isComplete(self, root, index, total_nodes):
        if not root:
            return True
        if index >= total_nodes:
            return False
        return (self.isComplete(root.left, 2 * index + 1, total_nodes) and
                self.isComplete(root.right, 2 * index + 2, total_nodes))

    def hasHeapProperty(self, root):
        if not root.left and not root.right:
            return True
        if not root.right:
            return root.data >= root.left.data and self.hasHeapProperty(root.left)
        else:
            return (root.data >= root.left.data and
                    root.data >= root.right.data and
                    self.hasHeapProperty(root.left) and
                    self.hasHeapProperty(root.right))

    def isHeap(self, root):
        if not root:
            return True
        
        total_nodes = self.countNodes(root)
        
        if self.isComplete(root, 0, total_nodes) and self.hasHeapProperty(root):
            return True
        else:
            return False
