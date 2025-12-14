"""
   Leetcode problem: 152. Maximum Product Subarray - medium
   Author: Peter Alexia
   Description:
   Given an integer array nums, find a subarray that has the largest product, and return the product.
   The test cases are generated so that the answer will fit in a 32-bit integer.
   Note that the product of an array with a single element is the value of that element.
   Date: 12.dec.2025
"""
import unittest
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for n in nums:
            temp = cur_max * n
            cur_max = max(temp, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)

            res = max(res, cur_max)

        return res


class TestMaxProduct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 3, -2, 4]
        expected = 6
        # Explanation: [2, 3] has the largest product 6.
        result = self.solution.maxProduct(nums)
        print(f"Test 1 Input: {nums} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [-2, 0, -1]
        expected = 0
        # Explanation: The result cannot be 2, because [-2, -1] is not a subarray.
        result = self.solution.maxProduct(nums)
        print(f"Test 2 Input: {nums} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_negative_flip(self):
        nums = [-2, 3, -4]
        expected = 24
        # Explanation: -2 * 3 * -4 = 24. The negative numbers flip the min to max.
        result = self.solution.maxProduct(nums)
        print(f"Test 3 Input: {nums} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [-2]
        expected = -2
        result = self.solution.maxProduct(nums)
        print(f"Test 4 Input: {nums} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()