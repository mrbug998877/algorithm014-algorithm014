#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        import collections
        if not root:
            return []
        ans = []
        queue = collections.deque([root,])
        while queue:
            curr_max = float('-inf')
            for _ in range (len(queue)):
                node = queue.popleft()
                curr_max = max(curr_max,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr_max)
        return ans

# @lc code=end

