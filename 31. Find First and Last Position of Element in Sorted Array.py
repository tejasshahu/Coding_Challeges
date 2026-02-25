"""
Find First and Last Position of Element in Sorted Array
Medium - difficulty
Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
from typing import List

class Solution:
    def lowerbound(self, nums, target):
        l = 0
        h = len(nums) - 1
        index = -1
        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                index = m
                h = m-1
            elif nums[m] > target:
                h = m-1
            else:
                l = m+1
        return index

    def higherbound(self, nums, target):
        l = 0
        h = len(nums) - 1
        index = -1
        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                index = m
                l = m+1
            elif nums[m] < target:
                l = m+1
            else:
                h = m-1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        first = self.lowerbound(nums, target)
        if first == -1:
            return [first, last]
        last = self.higherbound(nums, target)
        return [first, last]