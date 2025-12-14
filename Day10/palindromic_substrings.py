"""
   Leetcode problem: 647. Palindromic substrings - medium
   Author: Peter Alexia
   Description:
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.
   Date: 10.dec.2025
"""
import unittest


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # Odd length palindromes
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # Even length palindromes
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res


class TestPalindromicSubstrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # Test 1: Standard case with mixed characters
    def test_example_1(self):
        s = "abc"
        expected = 3
        # Explanation: "a", "b", "c"
        result = self.solution.countSubstrings(s)
        print(f"Test 1 Input: '{s}' | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    # Test 2: Case with repeating characters (overlapping palindromes)
    def test_example_2(self):
        s = "aaa"
        expected = 6
        # Explanation: "a", "a", "a", "aa", "aa", "aaa"
        result = self.solution.countSubstrings(s)
        print(f"Test 2 Input: '{s}' | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()