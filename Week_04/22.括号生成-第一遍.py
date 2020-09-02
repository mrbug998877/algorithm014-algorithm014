#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.generator(n,n,"")
        return self.ans

    def generator(self,left,right,curr):
        if left == right == 0:
            self.ans.append(curr)
            return
        if left:
            self.generator(left - 1, right, curr+'(')
        
        if right > left:
            self.generator(left,right-1,curr+')')
        



# @lc code=end

