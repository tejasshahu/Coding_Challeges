from typing import  List
from collections import defaultdict

# Brute Force Solution
class SolutionB:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            ans[key].append(s)

        return list(ans.values())
# Time: O(n * (m log m))
# Space: O(n * m)
# n is the number of strings, m is the length of largest string

# Optimal Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs: # n
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())
# n is the number of strings, m is the length of largest string
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

if __name__ == '__main__':
    s = SolutionB()
    input_list = ["eat","tea","tan","ate","nat","bat"]
    print(s.groupAnagrams(input_list))
    t = Solution()
    print(t.groupAnagrams(input_list))