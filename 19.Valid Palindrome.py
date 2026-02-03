class Solution:
    def isAlphaNumeric(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
        )

    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        i = 0
        j = l-1
        while i<j:
            while i < j and not self.isAlphaNumeric(s[i]):
                i += 1
            while i < j and not self.isAlphaNumeric(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i+1, j-1
        return True

if __name__ == '__main__':
    S = Solution()
    print(S.isPalindrome("A man, a plan, a canal: Panama"))