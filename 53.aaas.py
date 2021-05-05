# -*- coding:utf-8 -*-
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp_sum = 0
        res = nums[0]
        for num in nums:
            tmp_sum = max(tmp_sum + num, num)
            res = max(res, tmp_sum)
        return res

