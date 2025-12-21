"""
   Leetcode problem: 21. Merge Two Sorted Lists
   Author: Peter Alexia
   Description:
   You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together
    the nodes of the first two lists.
    Return the head of the merged linked list.

    Date: 19.dec.2025
"""
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next

# Helper Functions for Testing
def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Standard lists
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    merged = sol.mergeTwoLists(l1, l2)
    print(f"Test 1 - Input: [1,2,4], [1,3,4] | Output: {linked_list_to_list(merged)}")

    # Test Case 2: One empty list
    l1_empty = build_linked_list([])
    l2_single = build_linked_list([0])
    merged_2 = sol.mergeTwoLists(l1_empty, l2_single)
    print(f"Test 2 - Input: [], [0] | Output: {linked_list_to_list(merged_2)}")

    # Test Case 3: Both empty
    merged_3 = sol.mergeTwoLists(None, None)
    print(f"Test 3 - Input: [], [] | Output: {linked_list_to_list(merged_3)}")