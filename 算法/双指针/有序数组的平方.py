"""
给你一个按 非递减顺序 排序的整数数组nums,返回 每个数字的平方 组成的新数组,要求也按 非递减顺序 排序。

输入:nums = [-4,-1,0,3,10]; 输出:[0,1,9,16,100]
输入:nums = [-7,-3,2,3,11]; 输出:[4,9,9,49,121]
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num * num for num in nums)