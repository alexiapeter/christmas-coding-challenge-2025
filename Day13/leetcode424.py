"""
   Leetcode problem: 424. Longest Repeating Character Replacement - medium
   Author: Peter Alexia
   Description:
   You are given a string s and an integer k. You can choose any character of the string
    and change it to any other uppercase English character.
    You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter
    you can get after performing the above operations.
   Date: 13.dec.2025
"""
import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # (Window Length) - (Most Frequent Char Count) = Number of replacements needed
            # If replacements needed > k, shrink window from the left
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


class TestCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "ABAB"
        k = 2
        expected = 4
        # Explanation: Replace the two 'A's with 'B's or vice versa to get "BBBB" or "AAAA".
        result = self.solution.characterReplacement(s, k)
        print(f"Test 1 Input: s='{s}', k={k} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_example_2(self):
        s = "AABABBA"
        k = 1
        expected = 4
        # Explanation: Replace the one 'B' in the middle to form "AAAA" (substring length 4).
        result = self.solution.characterReplacement(s, k)
        print(f"Test 2 Input: s='{s}', k={k} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_no_replacements_needed(self):
        s = "AAAA"
        k = 2
        expected = 4
        result = self.solution.characterReplacement(s, k)
        print(f"Test 3 Input: s='{s}', k={k} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)

    def test_short_string(self):
        s = "A"
        k = 0
        expected = 1
        result = self.solution.characterReplacement(s, k)
        print(f"Test 4 Input: s='{s}', k={k} | Expected: {expected} | Got: {result}")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()