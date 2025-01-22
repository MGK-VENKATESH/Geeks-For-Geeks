Description:
Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers.

For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Examples:

Input: num1 = 4 - > 5, num2 = 3 -> 4 -> 5
Output:  3 -> 9 -> 0
 
Explanation: Given numbers are 45 and 345. There sum is 390.
Input: num1 = 0 -> 0 -> 6 -> 3, num2 = 0 -> 7 
Output: 7 -> 0 
 
Explanation: Given numbers are 63 and 7. There sum is 70.
Constraints:
1 <= size of both linked lists <= 106
0 <= elements of both linked lists <= 9
Python3:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def addTwoLists(self, num1, num2):
        # Reverse both lists
        num1 = self.reverseList(num1)
        num2 = self.reverseList(num2)

        carry = 0
        dummy = Node(0)
        current = dummy

        # Add digits and manage carry
        while num1 or num2 or carry:
            sum_value = carry
            if num1:
                sum_value += num1.data
                num1 = num1.next
            if num2:
                sum_value += num2.data
                num2 = num2.next

            carry = sum_value // 10
            current.next = Node(sum_value % 10)
            current = current.next

        # Reverse the result back
        result = self.reverseList(dummy.next)

        # Remove leading zeros
        while result and result.data == 0 and result.next:
            result = result.next

        return result
