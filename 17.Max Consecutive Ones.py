from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = len(nums)
        max_count, count = 0, 0
        for i in range(0, l):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        return max(count, max_count)


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
