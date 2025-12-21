"""
   Leetcode problem: 15. 3Sum - medium
   Author: Peter Alexia
   Description:
   Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
   such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets

   Date: 17.dec.2025
"""
from typing import List

class TestSolutions:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

# --- Execution Block ---
if __name__ == "__main__":
    tester = TestSolutions()

    print("\n--- Testing LeetCode 15 (3Sum) ---")
    list15 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: {list15} | Output: {tester.threeSum(list15)} | Expected: [[-1, -1, 2], [-1, 0, 1]]")