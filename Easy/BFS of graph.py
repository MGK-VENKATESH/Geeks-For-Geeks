Description:
Given a connected undirected graph containing V vertices, represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Search (BFS) traversal starting from vertex 0, visiting vertices from left to right according to the given adjacency list, and return a list containing the BFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list.

Examples:

Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output: [0, 2, 3, 1, 4]
Explanation: Starting from 0, the BFS traversal will follow these steps: 
Visit 0 → Output: 0 
Visit 2 (first neighbor of 0) → Output: 0, 2 
Visit 3 (next neighbor of 0) → Output: 0, 2, 3 
Visit 1 (next neighbor of 0) → Output: 0, 2, 3, 
Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4
Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

Output: [0, 1, 2, 3, 4]
Explanation: Starting from 0, the BFS traversal proceeds as follows: 
Visit 0 → Output: 0 
Visit 1 (the first neighbor of 0) → Output: 0, 1 
Visit 2 (the next neighbor of 0) → Output: 0, 1, 2 
Visit 3 (the first neighbor of 2 that hasn't been visited yet) → Output: 0, 1, 2, 3 
Visit 4 (the next neighbor of 2) → Final Output: 0, 1, 2, 3, 4
Constraints:
1 ≤ V = adj.size() ≤ 104
1 ≤ adj[i][j] ≤ 104

Company Tags
FlipkartAmazonMicrosoftSamsungOla CabsAdobeSAP Labs

Python3:
from collections import deque
from typing import List

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj: List[List[int]]) -> List[int]:
        V = len(adj)  # Number of vertices
        visited = set()  # Set to keep track of visited nodes
        queue = deque([0])  # BFS queue starting from vertex 0
        visited.add(0)
        result = []

        while queue:
            node = queue.popleft()  # Dequeue front element
            result.append(node)  # Store BFS traversal order
            
            for neighbor in adj[node]:  # Traverse neighbors in given order
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return result
