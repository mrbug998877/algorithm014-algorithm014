#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_A = 0
        j = len(height) - 1
        i = 0
        while i < j:
            if height[i] < height[j]:
                max_A = max(max_A,(j - i) * height[i])
                i += 1
            else:
                max_A = max(max_A,(j - i) * height[j])
                j -= 1
        return max_A
# @lc code=end

