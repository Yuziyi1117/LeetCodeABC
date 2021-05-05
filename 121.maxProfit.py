# -*- coding:utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # list_tmp1 = []
        # list_tmp2 = []
        # for i in range(0, len(prices)):
        #     for j in range(i, len(prices)):
        #         list_tmp1.append(prices[j] - prices[i])
        #     list_tmp1[i] = max(list_tmp1)
        #
        # res = max(list_tmp1)
        # if res < 0:
        #     return 0
        # else:
        #     return res

        dp0 = 0
        dp1 = -prices[0]
        dp2 = float("-inf")

        for i in range(1, len(prices)):
            dp1 = max(dp1, dp0 - prices[i])
            dp2 = max(dp2, dp1 + prices[i])
        return max(dp0, dp2)

s = Solution()
print(s.maxProfit([1,2,3,4,76]))