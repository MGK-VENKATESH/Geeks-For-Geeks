Description:
Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.

Examples:

Input: head = 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8, k = 4
Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5

Explanation: The first 4 elements 1, 2, 2, 4 are reversed first and then the next 4 elements 5, 6, 7, 8. Hence, the resultant linked list is 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5.
Input: head = 1 -> 2 -> 3 -> 4 -> 5, k = 3
Output: 3 -> 2 -> 1 -> 5 -> 4

Explanation: The first 3 elements 1, 2, 3 are reversed first and then left out elements 4, 5 are reversed. Hence, the resultant linked list is 3 -> 2 -> 1 -> 5 -> 4.
Constraints:
1 <= size of linked list <= 105
1 <= data of nodes <= 106
1 <= k <= size of linked list 
Python3:
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        g_s = None
        g_n = head
        g_p = None
        
        while g_n:
            
            k_s = g_n
            k_e = g_n
            
            cnt=0
            
            while cnt<k and g_n:
                cnt+=1
                k_e = g_n
                g_n = g_n.next
            
            curr=k_s
            prev=None
            
            # print(k_s.data,k_e.data)
            # print("---")
            
            while curr and curr!=g_n:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n
            
            if not g_s:
                g_s = prev
            
            if g_p:
                g_p.next = prev
                
            g_p = k_s
            
        return g_s
