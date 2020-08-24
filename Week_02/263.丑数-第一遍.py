#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num >= 5:
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                return False
            else:
                if num % 2 == 0:
                    num = num // 2
                elif num % 3 == 0:
                    num = num // 3
                else:
                    num = num // 5
        return True
# @lc code=end

