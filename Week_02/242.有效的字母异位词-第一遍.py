#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        if len (s) == len(t) ==0:
            return True 
        elif set(s) == set(t):
            for i in set(s):
                result = result and (s.count(i) == t.count(i))

        else:
            result = False
        return(result)

 
# @lc code=end

