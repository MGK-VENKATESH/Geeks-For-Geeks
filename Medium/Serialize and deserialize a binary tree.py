Description:
Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

serialize() : stores the tree into an array a and returns the array.
deSerialize() : deserializes the array to the tree and returns the root of the tree.
Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).

Examples :

Input: root = [1, 2, 3]
      
Output: [2, 1, 3]
Input: root = [10, 20, 30, 40, 60, N, N]
      
Output: [40, 20, 60, 10, 30]
Constraints:
1 <= Number of nodes <= 104
1 <= Data of a node <= 109

Python3:
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)  # Placeholder for missing nodes
        
        # Remove trailing None values (optional, to optimize storage)
        while result and result[-1] is None:
            result.pop()

        return result
    
    # Function to deserialize a list and construct the tree.   
    def deSerialize(self, arr):
        if not arr:
            return None
        
        root = Node(arr[0])
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            node = queue.popleft()
            
            # Process left child
            if i < len(arr) and arr[i] is not None:
                node.left = Node(arr[i])
                queue.append(node.left)
            i += 1

            # Process right child
            if i < len(arr) and arr[i] is not None:
                node.right = Node(arr[i])
                queue.append(node.right)
            i += 1
        
        return root
