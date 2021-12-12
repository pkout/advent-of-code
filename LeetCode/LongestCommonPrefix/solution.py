# pylint: disable=missing-function-docstring

from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        return self._longestCommonPrefix(strs, 0, len(strs) - 1)

    def _longestCommonPrefix(self, strs, l, r):
        if l == r:
            return strs[l]

        mid = (l + r) // 2
        left_common = self._longestCommonPrefix(strs, 0, mid)
        right_common = self._longestCommonPrefix(strs, mid + 1, r)

        return self._commonPrefix(left_common, right_common)


    def _commonPrefix(self, str1, str2):
        min_len = min(len(str1), len(str2))

        for i in range(min_len):
            if str1[i] != str2[i]:
                return str1[:i]

        return str1[:i+1]
