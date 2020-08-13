#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_sw = []
        for i in range (len(nums) - k + 1):
            if (i + k ) <= (len(nums)+1):
               max_sw.append(max(nums[i: (i+k)]))
               i += 1
        return max_sw

# @lc code=end

