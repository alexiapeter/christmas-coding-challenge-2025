"""
   Leetcode problem: 20. Valid Parentheses
   Author: Peter Alexia
   Description:
   Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
   determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

   Date: 18.dec.2025
"""
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in Map:
                if stack and stack[-1] == Map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

def run_tests():
    sol = Solution()

    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("[", False),
        ("]", False)
    ]

    print("LeetCode 20: Valid Parentheses ")
    for s, expected in test_cases:
        result = sol.isValid(s)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Input: '{s}' | Output: {result} | Expected: {expected} | {status}")


if __name__ == "__main__":
    run_tests()