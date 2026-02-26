"""
Given a sorted array, arr[] and a number target, you need to find the number
of occurrences of target in arr[].

Examples:

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.
Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ target ≤ 106

"""

class Solution:
    def lowerbound(self, arr, target):
        l = 0
        h = len(arr) - 1
        lb = -1
        while l <= h:
            m = (l + h) // 2
            if arr[m] >= target:
                lb = m
                h = m - 1
            else:
                l = m + 1
        return lb

    def higherbound(self, arr, target):
        l = 0
        h = len(arr) - 1
        hb = len(arr)
        while l <= h:
            m = (l + h) // 2
            if arr[m] > target:
                hb = m
                h = m - 1
            else:
                l = m + 1
        return hb

    def countFreq(self, arr, target):
        lb = self.lowerbound(arr, target)
        if lb == -1 or arr[lb] != target:
            return 0
        hb = self.higherbound(arr, target)
        return hb - lb

print(Solution().countFreq([1, 1, 2, 2, 2, 2, 3], 3))