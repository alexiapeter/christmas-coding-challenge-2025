"""
   Leetcode problem: 17. Letter Combinations of a Phone Number - medium
   Author: Peter Alexia
   Description:
   Given a string containing digits from 2-9 inclusive, return all possible
    letter combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.
   Date: 15.dec.2025
"""
import unittest
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {"2": "abc",
                       "3": "def",
                       "4": "ghi",
                       "5": "jkl",
                       "6": "mno",
                       "7": "qprs",
                       "8": "tuv",
                       "9": "wxyz"}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res


class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        digits = "23"
        # 2 -> "abc", 3 -> "def"
        # Combinations: ad, ae, af, bd, be, bf, cd, ce, cf
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        result = self.solution.letterCombinations(digits)
        print(f"Test 1 Input: '{digits}' | Expected: {expected} | Got: {result}")
        self.assertEqual(sorted(result), sorted(expected))

    def test_empty_string(self):
        digits = ""
        expected = []
        result = self.solution.letterCombinations(digits)
        print(f"Test 2 Input: '{digits}' | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_single_digit(self):
        digits = "2"
        expected = ["a", "b", "c"]
        result = self.solution.letterCombinations(digits)
        print(f"Test 3 Input: '{digits}' | Expected: {expected} | Got: {result}")
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()