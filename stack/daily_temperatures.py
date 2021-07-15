"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for
which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = list()

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                res[index] = i - index
            stack.append([i, v])

        return res

    def dailyTemperaturesBruteForce(self, temperatures: list[int]) -> list[int]:
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res[i] = j-i
                    break
        return res