"""
Input
nums =
[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target =
2

Use Testcase
Output
false
Expected
true
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        n = len(nums)
        high = n-1
        while low <= high:
            m = (low+high)//2
            if nums[m] == target:
                return True
            if nums[low] == nums[m] == nums[high]:
                low += 1
                high -= 1
                continue
            elif nums[m] <= nums[high]:
                if nums[m] <= target <= nums[high]:
                    low = m + 1
                else:
                    high = m - 1
            else:
                if nums[low] <= target <= nums[m]:
                    high = m - 1
                else:
                    low = m + 1
        return False