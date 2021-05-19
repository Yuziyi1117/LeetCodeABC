# -*- coding:utf-8 -*-

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if not nums:
#             return -1
#         left = 0
#         right = len(nums) - 1
#         while right > left:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[left] >= target:
#                 left = mid - 1
#             elif nums[right] >= target:
#                 right = mid + 1
#         return -1

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == "__main__":
    s = Solution()
    res = s.search([4, 5, 6, 7, 0, 1, 2, 3], 0)
    print(res)
