from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        m = len(nums)
        missing = (m*(m+1))/2 - s
        return int(missing)

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3,0,1]))
