Description:
Implement a Queue using Linked List. 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element)

Example 1:

Input:
Q = 5
Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation: n the first testcase
1 2 the queue will be {2}
1 3 the queue will be {2 3}
2   poped element will be 2 the
    queue will be {3}
1 4 the queue will be {3 4}
2   poped element will be 3.

Example 2:

Input:
Q = 4
Queries = 1 2 2 2 1 3 
Output: 2 -1
Explanation: In the second testcase 
1 2 the queue will be {2}
2   poped element will be {2} then
    the queue will be empty. 
2   the queue is empty and hence -1
1 3 the queue will be {3}.
Your Task:
Complete the function push() which takes an integer as input parameter and pop() which will remove and return an element(-1 if queue is empty).

Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Q <= 100
1 <= x <= 100

Python3:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    # Function to push an element into the queue.
    def push(self, item): 
        new_node = Node(item)
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Function to pop front element from the queue.
    def pop(self):
        if self.front is None:  # If the queue is empty
            return -1
        popped_value = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        return popped_value
