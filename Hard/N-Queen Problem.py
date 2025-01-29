Description:
The n-queens puzzle is the problem of placing n queens on a (n × n) chessboard such that no two queens can attack each other. Note that two queens attack each other if they are placed on the same row, the same column, or the same diagonal.

Given an integer n, find all distinct solutions to the n-queens puzzle.
You can return your answer in any order but each solution should represent a distinct board configuration of the queen placements, where the solutions are represented as permutations of [1, 2, 3, ..., n]. In this representation, the number in the ith position denotes the row in which the queen is placed in the ith column.
For eg. below figure represents a chessboard [3 1 4 2].



Examples:

Input: n = 1
Output: [1]
Explaination: Only one queen can be placed in the single cell available.
Input: n = 4
Output: [[2 4 1 3 ] [3 1 4 2 ]]
Explaination: There are 2 possible solutions for n = 4.
Input: n = 2
Output: []
Explaination: There are no possible solutions for n = 2.
Constraints:
1 ≤ n ≤ 10
Python3:
#User function Template for python3

class Solution:
    def nQueen(self, a):
        b = []
        
        def c(d, e, f, g, h):
            if d == a:
                b.append(h[:])
                return
            
            for i in range(a):
                if i in e or (d - i) in f or (d + i) in g:
                    continue
                
                e.add(i)
                f.add(d - i)
                g.add(d + i)
                h.append(i + 1)

                c(d + 1, e, f, g, h)

                e.remove(i)
                f.remove(d - i)
                g.remove(d + i)
                h.pop()
        
        c(0, set(), set(), set(), [])
        
        return b
        # code here
