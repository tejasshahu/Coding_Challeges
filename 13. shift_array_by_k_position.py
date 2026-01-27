from typing import List

def shift_array_by_1_position(n):
    temp = n[-1]
    for i in range(len(n)-2,0,-1):
        n[i+1] = n[i]
        print(n)
    n[0] = temp
    return n


class Solution:
    def reverse(self, nums: List[int], l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, n - k, n-1)
        self.reverse(nums, 0, n - k-1)
        self.reverse(nums, 0, n - 1)
        return nums


if __name__ == '__main__':
    n = [4, 4, 0, 1, 1, 1, 2, 2, 3, 3]
    k = 18
    a = n[len(n)-k:] + n[:len(n)-k]
    print("Rotated list using slicing:", a)
    s = Solution()
    nums = s.rotate(n, k)
    print("Optimized solution:", nums)
