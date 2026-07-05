"""
Problem: 21. Merge Two Sorted Lists

Difficulty: Easy

Topic:
- Linked List

Approach:
Both linked lists are already sorted.

Create a dummy node to serve as the start of the merged list
and use a pointer (current) to build the merged list.

Compare the current nodes of both lists:
- Attach the smaller node to the merged list.
- Move the corresponding list pointer forward.
- Move the current pointer forward.

Once one list becomes empty, attach the remaining nodes of the
other list directly since they are already sorted.

Finally, return dummy.next because the dummy node itself is not
part of the answer.

Time Complexity: O(n + m)

where:
n = length of list1
m = length of list2

Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next