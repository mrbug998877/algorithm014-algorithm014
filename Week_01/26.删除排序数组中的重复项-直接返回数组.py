#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newnums = sorted(nums)
        ori_len = len(nums)
        for i in range (ori_len):
            if i == 0:
                newnums.append(newnums[0])
            elif newnums[i] == newnums[i-1]:
                i += 1
            else:
                newnums.append(newnums[i])
        print (newnums[ori_len:])

# @lc code=end

