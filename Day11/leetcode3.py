"""
   Leetcode problem: 3. Longest Substring Without Repeating Characters - medium
   Author: Peter Alexia
   Description:
    Given a string s, find the length of the longest substring without duplicate characters.
   Date: 11.dec.2025
"""
import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "abcabcbb"
        expected = 3
        # Explanation: The answer is "abc", with the length of 3.
        result = self.solution.lengthOfLongestSubstring(s)
        print(f"Test 1 Input: '{s}' | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_example_2(self):
        s = "bbbbb"
        expected = 1
        # Explanation: The answer is "b", with the length of 1.
        result = self.solution.lengthOfLongestSubstring(s)
        print(f"Test 2 Input: '{s}' | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_example_3(self):
        s = "pwwkew"
        expected = 3
        # Explanation: The answer is "wke", with the length of 3.
        # Note that the answer must be a substring, "pwke" is a subsequence.
        result = self.solution.lengthOfLongestSubstring(s)
        print(f"Test 3 Input: '{s}' | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        expected = 0
        result = self.solution.lengthOfLongestSubstring(s)
        print(f"Test 4 Input: '{s}' | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()