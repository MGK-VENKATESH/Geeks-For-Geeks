Description:
Given q queries, You task is to implement the following four functions for a stack:

push(x) – Insert an integer x onto the stack.
pop() – Remove the top element from the stack.
peek() - Return the top element from the stack. If the stack is empty, return -1.
getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
Each query can be one of the following:

1 x : Push x onto the stack.
2 : Pop the top element from the stack.
3: Return the top element from the stack. If the stack is empty, return -1.
4: Return the minimum element from the stack.
Examples:

Input: q = 7, queries = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
Output: [3, 2, 1]
Explanation: 
push(2): Stack is [2]
push(3): Stack is [2, 3]
peek(): Top element is 3
pop(): Removes 3, stack is [2]
getMin(): Minimum element is 2
push(1): Stack is [2, 1]
getMin(): Minimum element is 1
Input: q = 4, queries = [[1, 4], [1, 2], [4], [3]]
Output: [2, 2]
Explanation: 
push(4): Stack is [4]
push(2): Stack is [4, 2]
getMin(): Minimum element is 2
peek(): Top element is 2
Input: q = 5, queries = [[1, 10], [4], [1, 5], [4], [2]]
Output: [10, 5]
Explanation: 
push(10): Stack is [10]
getMin(): Minimum element is 10
push(5): Stack is [10, 5]
getMin(): Minimum element is 5
pop(): Removes 5, stack is [10]
Constraints:
1 <= q <= 105
0 <= values on the stack <= 109

Python3:
class Solution:
    def __init__(self):
        self.stack = []      # Main stack
        self.min_stack = []  # Min stack to keep track of minimum elements

    # Push x onto the stack
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    # Remove top element from stack
    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    # Return the top element from stack
    def peek(self):
        return self.stack[-1] if self.stack else -1

    # Retrieve the minimum element in O(1) time
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else -1

# Function to process queries
def processQueries(q, queries):
    sol = Solution()
    result = []
    
    for query in queries:
        if query[0] == 1:
            sol.push(query[1])
        elif query[0] == 2:
            sol.pop()
        elif query[0] == 3:
            result.append(sol.peek())
        elif query[0] == 4:
            result.append(sol.getMin())

    return result

# Example Usage
print(processQueries(7, [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]))  # Output: [3, 2, 1]
print(processQueries(4, [[1, 4], [1, 2], [4], [3]]))  # Output: [2, 2]
print(processQueries(5, [[1, 10], [4], [1, 5], [4], [2]]))  # Output: [10, 5]
