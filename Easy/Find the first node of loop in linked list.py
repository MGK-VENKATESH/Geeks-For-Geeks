Description:
Given a head of the singly linked list. If a loop is present in the list then return the first node of the loop else return NULL.

Custom Input format:
A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

Examples:

Input:
 
Output: 3
Explanation: We can see that there exists a loop in the given linked list and the first node of the loop is 3.
Input:
 
Output: -1
Explanation: No loop exists in the above linked list.So the output is -1.
Constraints:
1 <= no. of nodes <= 106
1 <= node->data <= 106 
Python3:
class Solution:
    def findFirstNode(self, head):
        node_set = set()
        while head:
            if head in node_set:
                return head
            node_set.add(head)
            head = head.next
        return None
