Description:
You are given an undirected graph with V vertices and E edges. The graph is represented as a 2D array edges[][], where each element edges[i] = [u, v] indicates an undirected edge between vertices u and v.
Your task is to return all the articulation points (or cut vertices) in the graph.
An articulation point is a vertex whose removal, along with all its connected edges, increases the number of connected components in the graph.

Note: The graph may be disconnected, i.e., it may consist of more than one connected component.
If no such point exists, return {-1}.

Examples :

Input: V = 5, edges[][] = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]

Output: [1, 4]
Explanation: Removing the vertex 1 or 4 will disconnects the graph as-
   
Input: V = 4, edges[][] = [[0, 1], [0, 2]]
Output: [0]
Explanation: Removing the vertex 0 will increase the number of disconnected components to 3.  
Constraints:
1 ≤ V, E ≤ 104


Python3:
class Solution:

    def articulationPoints(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        time = [-1] * V
        low = [-1] * V
        critical = [False] * V
        timer = 0

        def dfs(node, parent):
            nonlocal timer
            time[node] = low[node] = timer
            timer += 1
            children = 0

            for nbr in adj[node]:
                if nbr == parent:
                    continue

                if low[nbr] == -1:
                    dfs(nbr, node)
                    children += 1
                    low[node] = min(low[node], low[nbr])
                    if low[nbr] >= time[node] and parent != -1:
                        critical[node] = True
                else:
                    low[node] = min(low[node], time[nbr])

            if children > 1 and parent == -1:
                critical[node] = True

        for i in range(V):
            if low[i] == -1:
                dfs(i, -1)

        ans = [i for i, val in enumerate(critical) if val]
        if not ans:
            return [-1]
        return sorted(ans)
