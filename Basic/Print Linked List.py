Description:
Given a linked list. Print all the elements of the linked list separated by space followed.

Examples:

Input: LinkedList : 1 -> 2

Output: 1 2
Explanation: The linked list contains two elements 1 and 2.The elements are printed in a single line.
Input: Linked List : 49 -> 10 -> 30
 
Output: 49 10 30
Explanation: The linked list contains 3 elements 49, 10 and 30. The elements are printed in a single line.
Expected Time Complexity: O(n)
Expected Auxiliary Space : O(1)
 
Python3:
class Solution:
    # Function to display the elements of a linked list in the same line
    def printList(self, head):
        current = head  # Start from the head node
        result = []  # Collect all node values
        while current:
            result.append(str(current.data))  # Append each node's data as a string
            current = current.next
        print(" ".join(result), end="")  # Print all values joined by a space
