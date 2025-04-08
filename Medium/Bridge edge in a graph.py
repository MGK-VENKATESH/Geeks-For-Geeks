Description:
Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u,v] represents the edge between the vertices u and v. Determine whether a specific edge between two vertices (c, d) is a bridge.

Note:

An edge is called a bridge if removing it increases the number of connected components of the graph.
if there’s only one path between c and d (which is the edge itself), then that edge is a bridge.
Examples :

Input:

c = 1, d = 2
Output: true
Explanation: From the graph, we can clearly see that blocking the edge 1-2 will result in disconnection of the graph.
Hence, it is a Bridge.
Input:

c = 0, d = 2
Output: false
Explanation:

Blocking the edge between nodes 0 and 2 won't affect the connectivity of the graph.
So, it's not a Bridge Edge. All the Bridge Edges in the graph are marked with a blue line in the above image.
Constraints:
1 ≤ V, E ≤ 105
0 ≤ c, d ≤ V-1

Python3:
from collections import defaultdict

class Solution:
    def isBridge(self, V, edges, c, d):
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * V

        # Step 2: DFS ignoring the edge (c, d)
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if (u == c and v == d) or (u == d and v == c):
                    continue  # skip the edge c-d
                if not visited[v]:
                    dfs(v)

        dfs(c)

        # Step 3: After DFS, if d is not visited, (c, d) was a bridge
        return not visited[d]
