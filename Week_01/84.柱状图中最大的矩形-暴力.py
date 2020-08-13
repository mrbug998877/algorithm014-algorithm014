#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
#baoli
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        total_area = []
        if len(heights) == 0:
            return 0
        elif len(heights) == 1:
            return heights[0]
        else:
            for i in range(len(heights) - 1):
                for j in range(i+1, len(heights) - 1):
                    if heights[j] >= heights[i] and j < len(heights) - 1 :
                        j += 1
                    else:
                        _area = heights [i] * (j - i)
                        total_area.append(_area)
                        i += 1
            return max(total_area)


# @lc code=end

