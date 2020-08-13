#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"]":"[", "}":"{", ")":"("}
        for symb in s:
            if symb in dic.values():
                stack.append(symb)
            elif symb in dic.keys():
                if stack == [] or dic[symb] != stack.pop():
                    return False
            else:
                return False
        return stack == []

                    
# @lc code=end

