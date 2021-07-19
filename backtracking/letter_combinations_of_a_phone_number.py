"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9']
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Time Complexity ~3^n where n is the number of letters
        # Space Complexity ~3^len(digits)
        res = list()
        if len(digits) == 0 or digits is None:
            return res

        mapping = [
            '0',
            '1',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]

        self.letters_combination(res, digits, "", 0, mapping)

        return res

    def letters_combination(self, res, digits, cur, index, mapping):
        if len(cur) == len(digits):
            res.append(cur)
            return

        letters = mapping[int(digits[index])]

        for c in letters:
            self.letters_combination(res, digits, cur + c, index + 1, mapping)