from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        maxi = float("-inf")
        total = 0
        for i in range(0, l):
            total = total + nums[i]
            maxi = max(total, maxi)
            if total < 0:
                total = 0
        return maxi

if __name__ == '__main__':
    S = Solution()
    print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))