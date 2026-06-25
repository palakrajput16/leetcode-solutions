"""
Problem: 2. Add Two Numbers

Difficulty: Medium

Topic:
- Linked List

Approach:
Traverse both linked lists simultaneously while maintaining
a carry value. At each step, add the corresponding digits,
create a new node containing the current digit, and update
the carry. Continue until both lists and the carry are exhausted.

Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry

            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next