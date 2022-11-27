"""
给定一个n个元素有序的（升序）整型数组nums和一个目标值target，写一个函数搜索nums中的target，如果目标值存在返回下标，否则返回-1。

输入: nums = [-1,0,3,5,9,12], target = 9; 输出: 4
输入: nums = [-1,0,3,5,9,12], target = 2; 输出: -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


result = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(result.search(nums, target))
nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(result.search(nums, target))
