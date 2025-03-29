Description:
You are given two arrays: deadline[], and profit[], which represent a set of jobs, where each job is associated with a deadline, and a profit. Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. You will earn the profit associated with a job only if it is completed by its deadline.

Your task is to find:

The maximum number of jobs that can be completed within their deadlines.
The total maximum profit earned by completing those jobs.
Examples :

Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: [2, 60]
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).
Input: deadline[] = [2, 1, 2, 1, 1], profit[] = [100, 19, 27, 25, 15]
Output: [2, 127]
Explanation: Job1 and Job3 can be done with maximum profit of 127 (100+27).
Input: deadline[] = [3, 1, 2, 2], profit[] = [50, 10, 20, 30]
Output: [3, 100]
Explanation: Job1, Job3 and Job4 can be completed with a maximum profit of 100 (50 + 20 + 30).
Constraints:
1 ≤ deadline.size() == profit.size() ≤ 105
1 ≤ deadline[i] ≤ deadline.size()
1 ≤ profit[i] ≤ 500

Python3:
class Solution:
    def find(self, parent, x):
        """Finds the latest available slot using path compression."""
        if parent[x] == x:
            return x
        parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    def jobSequencing(self, deadline, profit):
        # Step 1: Pair jobs as (profit, deadline) and sort in descending order of profit
        jobs = sorted(zip(profit, deadline), reverse=True, key=lambda x: x[0])

        # Step 2: Find the maximum deadline
        max_deadline = max(deadline)

        # Step 3: Create DSU parent array (initially each slot points to itself)
        parent = list(range(max_deadline + 1))

        max_profit = 0
        job_count = 0

        # Step 4: Iterate through sorted jobs
        for p, d in jobs:
            # Find the latest available slot before or at deadline
            available_slot = self.find(parent, d)
            if available_slot > 0:  # If a valid slot exists
                job_count += 1
                max_profit += p
                parent[available_slot] = self.find(parent, available_slot - 1)  # Union (allocate slot)

        return [job_count, max_profit]
