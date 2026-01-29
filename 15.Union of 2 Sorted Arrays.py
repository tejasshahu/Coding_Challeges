class Solution:
    def findUnion(self, a, b):
        result = []
        m = len(a)
        n = len(b)
        i, j = 0, 0
        while i<m and j<n:
            if a[i] <= b[j]:
                if len(result) == 0 or a[i] != result[-1]:
                    result.append(a[i])
                i += 1
            else:
                if len(result) == 0 or b[j] != result[-1]:
                    result.append(b[j])
                j += 1
        while i < m:
            if len(result) == 0 or a[i] != result[-1]:
                result.append(a[i])
            i += 1
        while j < n:
            if len(result) == 0 or b[j] != result[-1]:
                result.append(b[j])
            j += 1
        return result

if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3]
    s.findUnion(a, b)
