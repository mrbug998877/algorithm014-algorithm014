#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
#第一遍刷
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tri_list = []
        if len(nums) >= 3:
            for i in range (len(nums)-1):
                for j in range (i+1,len(nums)):
                    _sum = nums[i] + nums[j]
                    if (0 - _sum) in nums and (0 - _sum) != nums[i] and (0 - _sum) != nums[j]:
                        tri_list.append(sorted([nums[i],nums[j],0 - _sum]))
                    if (0 - _sum) == nums[i] == nums[j] and nums.count(0) >=3:
                        tri_list.append(sorted([nums[i],nums[j],0 - _sum]))
            return list(set([tuple(t) for t in tri_list]))
        else:
            return []
# @lc code=end

