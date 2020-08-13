#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            zero = nums.index(0)
            for i in range (len(nums)):
                if nums[i] != 0 and i > zero:
                    nums[i],nums[zero] = nums[zero], nums[i]
                    zero += 1
            return(nums)
        else:
            return(nums)
# @lc code=end

