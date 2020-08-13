#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        else:
            stack = []
            dict = {"]":"[", "}":"{", ")":"("}
            for i in s:
                if i in dict.values():
                    stack.append(i)
                elif i in dict.keys():
                    if stack == [] or dict[i] != stack.pop():
                        return False
                else:
                    return False
        return stack == []
# @lc code=end

