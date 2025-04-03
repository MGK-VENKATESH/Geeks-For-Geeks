Description:
Given a matrix mat[][] of dimension n * m where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

Note: Your task is to return the minimum time to rot all the fresh oranges. If not possible returns -1.

Examples:

Input: mat[][] = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
Output: 1
Explanation: Oranges at positions (0,2), (1,2), (2,0) will rot oranges at (0,1), (1,1), (2,2) and (2,1) in unit time.
Input: mat[][] = [[2, 2, 0, 1]]
Output: -1
Explanation: Oranges at (0,0) and (0,1) can't rot orange at (0,3).
Input: mat[][] = [[2, 2, 2], [0, 2, 0]]
Output: 0
Explanation: There is no fresh orange. 
Constraints:
1 ≤ mat.size() ≤ 500
1 ≤ mat[0].size() ≤ 500
mat[i][j] = {0, 1, 2} 

Python3:
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        if not mat:
            return -1
        
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        fresh_count = 0
        
        # Step 1: Add all rotten oranges to queue and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif mat[i][j] == 1:
                    fresh_count += 1
        
        # Edge case: No fresh oranges, return 0
        if fresh_count == 0:
            return 0
        
        # Step 2: BFS Traversal
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_time = 0

        while queue:
            i, j, time = queue.popleft()
            max_time = max(max_time, time)

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and mat[ni][nj] == 1:
                    mat[ni][nj] = 2  # Rot the fresh orange
                    fresh_count -= 1  # Decrease fresh count
                    queue.append((ni, nj, time + 1))  # Push with new time

        # Step 3: Check if all fresh oranges are rotten
        return max_time if fresh_count == 0 else -1



#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends
