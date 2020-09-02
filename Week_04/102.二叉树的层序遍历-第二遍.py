#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        # traverse in order level, keeping track of (row number, current node)
        queue = deque([(0, root)])
        # keep track of the nodes in each row
        d = {}

        while queue:
            row, node = queue.popleft()
            if node:
                d[row] = d.get(row, []) + [node.val]
                queue += (row+1, node.left), (row+1, node.right)

        # return a list of lists containing node values in increasing order with respect to the row number
        return [d[row] for row in sorted(d.keys())]

# @lc code=end

