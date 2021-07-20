"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""

1 <= s.length <= 500
s consists of lowercase English letters.
"""
from collections import Counter
from heapq import heappush, heappop, heapify


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = list()
        hashmap = Counter(s)
        heap = [(-value, key) for key, value in hashmap.items()]
        heapify(heap)

        p_a, p_b = 0, ''

        while heap:
            a, b = heappop(heap)
            res.append(b)
            if p_a < 0:
                heappush(heap, (p_a, p_b))
            a += 1
            p_a, p_b = a, b

        res = ''.join(res)

        if len(res) == len(s):
            return res
        else:
            return ''