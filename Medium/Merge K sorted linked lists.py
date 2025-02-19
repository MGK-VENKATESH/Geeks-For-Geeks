Description:
Given an array arr[] of n sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list, then return the head of the merged linked list.

Examples:

Input: arr[] = [1 -> 2 -> 3, 4 -> 5, 5 -> 6, 7 -> 8]
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> 7 -> 8
Explanation:
The arr[] has 4 sorted linked list of size 3, 2, 2, 2.
1st list: 1 -> 2-> 3
2nd list: 4 -> 5
3rd list: 5 -> 6
4th list: 7 -> 8
The merged list will be:
 
Input: arr[] = [1 -> 3, 8, 4 -> 5 -> 6]
Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8
Explanation:
The arr[] has 3 sorted linked list of size 2, 3, 1.
1st list: 1 -> 3
2nd list: 8
3rd list: 4 -> 5 -> 6
The merged list will be:

Constraints
1 <= total no. of nodes <= 105
1 <= node->data <= 103

Python3:
import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def mergeKLists(self, arr):
        min_heap = []
        
        # Push the first node of each list into the heap
        for i in range(len(arr)):
            if arr[i]:  # Ensure the list is not empty
                heapq.heappush(min_heap, (arr[i].data, i, arr[i]))  # (value, index, node)
        
        dummy = Node(0)  # Dummy node to simplify the linked list creation
        current = dummy

        while min_heap:
            value, i, node = heapq.heappop(min_heap)  # Get the smallest node
            current.next = node
            current = current.next  # Move forward
            
            if node.next:  # If there are more nodes in the current list, push them
                heapq.heappush(min_heap, (node.next.data, i, node.next))
        
        return dummy.next  # Return the merged sorted linked list

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

