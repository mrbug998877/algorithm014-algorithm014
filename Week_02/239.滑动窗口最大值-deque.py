#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        ans = []
        tem = deque()
        for i, n in enumerate(nums):
            while tem and nums[tem[-1]] <= n:
                tem.pop()
            tem += [i]
            if i - tem[0] >= k:
                tem.popleft()
            if i + 1 >= k:
                ans.append(nums[tem[0]])
        return ans
# @lc code=end

