Description:
Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Examples:

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
Explanation: 
 
1 -> 2 -> 0 -> 1 is a cycle.
Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
Output: false
Explanation: 
 
No cycle in the graph.
Constraints:
1 ≤ V ≤ 105
1 ≤ E = edges.size() ≤ 105

Python3:
from collections import deque, defaultdict

class Solution:
    def isCycle(self, V, edges):
        # Step 1: Create adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * V
        
        # Step 2: BFS for each unvisited node
        for i in range(V):
            if not visited[i]:
                if self.bfs(i, adj, visited):
                    return True  # Cycle found
        return False  # No cycle

    def bfs(self, start, adj, visited):
        queue = deque()
        queue.append((start, -1))  # (node, parent)
        visited[start] = True

        while queue:
            node, parent = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    # Visited neighbor that's not the parent → cycle
                    return True
        return False
