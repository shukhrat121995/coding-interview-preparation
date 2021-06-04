"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            # first you can use this method
            heapq.heappushpop(heap, num)
            # or you can use this one
            # heapq.heappush(heap, num)
            # if len(heap) > k:
            #     heapq.heappop(heap)

        return heapq.heappop(heap)