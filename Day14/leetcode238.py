"""
   Leetcode problem: 238. Product of Array Except Self - medium
   Author: Peter Alexia
   Description:
   Given an integer array nums, return an array answer such that answer[i]
   is equal to the product of all the elements of nums except nums[i].
   The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
   You must write an algorithm that runs in O(n) time and without using the division operation.
   Date: 14.dec.2025
"""
import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        # Explanation:
        # Index 0: 2*3*4 = 24
        # Index 1: 1*3*4 = 12
        # Index 2: 1*2*4 = 8
        # Index 3: 1*2*3 = 6
        result = self.solution.productExceptSelf(nums)
        print(f"Test 1 Input: {nums} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_with_zero(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        # Explanation: Any product not including the 0 will be 0.
        # Only the position of the 0 (index 2) gets the product of the rest (-1*1*-3*3 = 9).
        result = self.solution.productExceptSelf(nums)
        print(f"Test 2 Input: {nums} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_multiple_zeros(self):
        nums = [0, 2, 3, 0]
        expected = [0, 0, 0, 0]
        # Explanation: Every calculation will involve at least one zero.
        result = self.solution.productExceptSelf(nums)
        print(f"Test 3 Input: {nums} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()