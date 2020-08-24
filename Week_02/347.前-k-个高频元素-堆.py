#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections, heapq
        count = collections.Counter(sorted(nums))
        return heapq.nsmallest(k,count,key=lambda num: (-count[num],num))
# @lc code=end

