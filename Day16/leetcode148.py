"""
   Leetcode problem: 128. Longest Consecutive Sequence - medium
   Author: Peter Alexia
   Description:
   Given an unsorted array of integers nums, return the length of the longest
   consecutive elements sequence.
   You must write an algorithm that runs in O(n) time.
   Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
        Therefore, its length is 4.
   Date: 16.dec.2025
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # Check if 'n' is the start of a sequence.
            if (n - 1) not in numSet:
                length = 1
                # Expand the sequence upwards.
                while (n + length) in numSet:
                    length += 1
                #Track the maximum length found.
                if length > longest:
                    longest = length
        return longest
    
def run_tests():
    sol = Solution()

    test1 = [100, 4, 200, 1, 3, 2]
    expected1 = 4

    test2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    expected2 = 9

    test3 = []
    expected3 = 0

    test_cases = [
        ("Test 1 (Mixed)", test1, expected1),
        ("Test 2 (Long)", test2, expected2),
        ("Test 3 (Empty)", test3, expected3)
    ]

    print("Running LeetCode 128 Tests")
    for name, nums, expected in test_cases:
        result = sol.longestConsecutive(nums)
        status = "PASSED" if result == expected else "FAILED"
        print(f"{name}: {status} | Input: {nums} | Output: {result} | Expected: {expected}")


if __name__ == "__main__":
    run_tests()