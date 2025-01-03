Description:
Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the popped element. If the queue is empty then return -1)

We just have to implement the functions push and pop and the driver code will handle the output.

Examples:

Input: Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation: For query 1 2 the queue will be {2} 1 3 the queue will be {2 3} 2   poped element will be 2 the queue will be {3} 1 4 the queue will be {3 4} 2 poped element will be 3 
Input: Queries = 1 3 2 2 1 4   
Output: 3 -1
Explanation: For query 1 3 the queue will be {3} 2 poped element will be 3 the queue will be empty 2 there is no element in the queue and hence -1 1 4 the queue will be {4}. 
Input: Queries = 1 3 2 2 1 3   
Output: 3 -1
Explanation: For query 1 3 the queue will be {3} 2 poped element will be 3 the queue will be empty 2 there is no element in the queue and hence -1 1 3 the queue will be {3} and hence -1 1 3 the queue will be {3}.
Constraints:
1 ≤ number of query≤ 105
0 ≤ x ≤ 105
Python3:
class MyQueue:
    def __init__(self):
        # Initialize an empty list to simulate the queue
        self.queue = []
    
    # Function to push an element x in a queue
    def push(self, x):
        # Append the element to the end of the queue
        self.queue.append(x)
    
    # Function to pop an element from queue and return that element
    def pop(self): 
        # Check if the queue is empty
        if len(self.queue) == 0:
            return -1
        # Pop the first element of the queue
        return self.queue.pop(0)
