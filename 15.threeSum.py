# -*- coding:utf-8 -*-

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        k = 0
        for k in range(0, len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -=1
                elif s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i +=1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -=1
                    while i < j and nums[i] == nums[i - 1]: i +=1
        return res


s = Solution()
nums = [0,0,0]
res = s.threeSum(nums)

print(res)