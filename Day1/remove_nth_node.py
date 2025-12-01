"""
   Leetcode problem: 19.Remove nth Node from a Linked List - medium
   Author: Peter Alexia
   Description: Given the head of a linked list, remove the nth node
                from the end of the list and return its head.
   Date: 1.dec.2025
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of the list and returns the head.
        Uses the Two-Pointer (Fast/Slow Runner) technique.
        """
        # Create a dummy node to handle the edge case where the head is removed.
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Advance the 'fast' pointer 'n' steps ahead to create the gap.
        for _ in range(n):
            if fast is None:
                # This check is mostly for robustness, though constraints usually guarantee validity.
                return head
            fast = fast.next

        # Move both pointers until 'fast.next' is None.
        # This means 'fast' is at the last node, and 'slow' is one node before the target.
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Remove the target node.
        # The target is slow.next. We bypass it by pointing slow.next to slow.next.next.
        slow.next = slow.next.next

        # Return the new head of the list.
        return dummy.next


# --- Helper Functions for Testing ---

def list_to_linkedlist(arr: list) -> Optional[ListNode]:
    """Converts a Python list to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head: Optional[ListNode]) -> list:
    """Converts a linked list back to a Python list for easy verification."""
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


# --- Example Usage ---

if __name__ == "__main__":
    solution = Solution()

    # Example 1: head = [1, 2, 3, 4, 5], n = 2 -> Output: [1, 2, 3, 5]
    list1 = [1, 2, 3, 4, 5]
    n1 = 2
    head1 = list_to_linkedlist(list1)
    result_head1 = solution.removeNthFromEnd(head1, n1)
    result_list1 = linkedlist_to_list(result_head1)
    print(f"Input: {list1}, n = {n1}")
    print(f"Output: {result_list1}")
    print("-" * 20)

    # Example 2: head = [1], n = 1 -> Output: []
    list2 = [1]
    n2 = 1
    head2 = list_to_linkedlist(list2)
    result_head2 = solution.removeNthFromEnd(head2, n2)
    result_list2 = linkedlist_to_list(result_head2)
    print(f"Input: {list2}, n = {n2}")
    print(f"Output: {result_list2}")
    print("-" * 20)

    # Example 3: head = [1, 2], n = 1 -> Output: [1]
    list3 = [1, 2]
    n3 = 1
    head3 = list_to_linkedlist(list3)
    result_head3 = solution.removeNthFromEnd(head3, n3)
    result_list3 = linkedlist_to_list(result_head3)
    print(f"Input: {list3}, n = {n3}")
    print(f"Output: {result_list3}")
    print("-" * 20)

    # Custom Edge Case: Remove the head (n = length)
    list4 = [10, 20, 30]
    n4 = 3
    head4 = list_to_linkedlist(list4)
    result_head4 = solution.removeNthFromEnd(head4, n4)
    result_list4 = linkedlist_to_list(result_head4)
    print(f"Input: {list4}, n = {n4} (Remove Head)")
    print(f"Output: {result_list4}")
    print("-" * 20)