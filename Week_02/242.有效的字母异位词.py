#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        count = collections.Counter(s)
        if count == collections.Counter(t):
            return True
        else:
            return False
# @lc code=end

