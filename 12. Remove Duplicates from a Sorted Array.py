"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        i = 0
        j = i + 1
        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        print(nums)
        return i+1

sol = Solution()
print(sol.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))