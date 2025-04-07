Description:
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v.

Examples:

Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 3], [3, 3]]



Output: true
Explanation: 3 -> 3 is a cycle
Input: V = 3, edges[][] = [[0, 1], [1, 2]]



Output: false
Explanation: no cycle in the graph
Constraints:
1 ≤ V, E ≤ 105

Python3:
from collections import defaultdict

class Solution:
    def isCycle(self, V, edges):
        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V
        recStack = [False] * V

        # Step 2: DFS with recursion stack
        def dfs(v):
            visited[v] = True
            recStack[v] = True

            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True

            recStack[v] = False
            return False

        # Step 3: Try DFS from every node
        for node in range(V):
            if not visited[node]:
                if dfs(node):
                    return True

        return False


