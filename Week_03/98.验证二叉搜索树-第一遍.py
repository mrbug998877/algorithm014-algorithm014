#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(root,min_val,max_val):
            if root == None:
                return True
            if root.val >= max_val or root.val <= min_val:
                return False
            return isBST(root.left, min_val,root.val) and isBST(root.right,root.val,max_val)
        return isBST(root,float("-inf"),float("inf"))
# @lc code=end

