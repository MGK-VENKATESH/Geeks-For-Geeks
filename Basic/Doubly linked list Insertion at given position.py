Description:
Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list and return the head of the updated list.

Examples:

Input: LinkedList: 2<->4<->5, p = 2, x = 6 
Output: 2<->4<->5<->6
Explanation: p = 2, and x = 6. So, 6 is inserted after p, i.e, at position 2 (0-based indexing).
Input: LinkedList: 1<->2<->3<->4, p = 0, x = 44
Output: 1<->44<->2<->3<->4
Explanation: p = 0, and x = 44 . So, 44 is inserted after p, i.e, at position 0 (0-based indexing).
Constraints:
0 <= p < size of doubly linked list <= 106
1 <= x <= 106
Python3:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    # Function to insert a new node at a given position in a doubly linked list.
    def addNode(self, head, p, x):
        # Create the new node
        new_node = Node(x)
        
        # Traverse to the p-th node
        current = head
        for _ in range(p):
            current = current.next
        
        # Insert the new node after the p-th node
        new_node.next = current.next  # Connect new node to the next node
        if current.next:  # If not the last node, update the next node's prev pointer
            current.next.prev = new_node
        current.next = new_node  # Connect p-th node to the new node
        new_node.prev = current  # Set the new node's prev pointer to the current node
        
        return head  # Return the updated head of the list
