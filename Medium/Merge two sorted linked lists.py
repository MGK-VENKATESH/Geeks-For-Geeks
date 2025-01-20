Description:
Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list.

Examples:

Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40
Explanation:

Input: head1 = 1 -> 1, head2 = 2 -> 4
Output: 1 -> 1 -> 2 -> 4
Explanation:

Constraints:
1 <= no. of nodes<= 103
0 <= node->data <= 105

Python3:
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        arr= []
        while head1 is not None:
            arr.append(head1.data)
            head1 = head1.next
        while head2 is not None:
            arr.append(head2.data)
            head2 = head2.next
        arr.sort()
        dummy = Node(-1)
        curr = dummy
        
        for value in arr:
            curr.next = Node(value)
            curr = curr.next
        return dummy.next
    def printlist(curr):
        while curr is not Null:
            print(curr.data, end = " ")
            curr = curr.next
        print()
