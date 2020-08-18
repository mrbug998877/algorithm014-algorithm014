#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return[]
        stack, res = [(0,root)], []
        while stack:
            flag, node = stack.pop()
            if not node: continue
            if flag == 1:
                res.append(node.val)
            else:
                stack.append((1,node))
                stack.append((0,node.right))
                stack.append((0,node.left))
        return res


# @lc code=end

