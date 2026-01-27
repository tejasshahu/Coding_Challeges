from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 1 or l == 0:
            return
        i = 0
        while i < l:
            if nums[i] == 0:
                break
            i += 1
            if i == n:
                return
        j = i + 1
        while j < l:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        print(nums)
        return

if __name__ == '__main__':
    s = Solution()
    n = [0, 1, 2, 3]
    s.moveZeroes(n)
