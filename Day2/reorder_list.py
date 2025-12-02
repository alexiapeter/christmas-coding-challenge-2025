"""
   Leetcode problem: 143. Reorder List - medium
   Author: Peter Alexia
   Description:
    You are given the head of a singly linked-list.
    The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.
   Date: 2.dec.2025
"""

#Example
#Input: head = [1,2,3,4,5]
#Output: [1,5,2,4,3]
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Find middle
        one, two = head, head
        while two and two.next:
            one = one.next
            two = two.next.next

        # Reverse second half
        prev = None
        curr = one.next
        one.next = None  # cut the list into two halves
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev now points to the head of reversed half

        # Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2