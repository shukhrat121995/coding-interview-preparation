"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Input: num1 = "11", num2 = "123"
Output: "134"

Input: num1 = "456", num2 = "77"
Output: "533"

Input: num1 = "0", num2 = "0"
Output: "0"

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = list()
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0

        while i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                total += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                total += ord(num2[j]) - ord('0')
                j -= 1

            res.append(total % 10)
            carry = total // 10

        if carry > 0:
            res.append(carry)

        return "".join(map(str, res[::-1]))