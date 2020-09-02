#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        type start :str
        tyoe end : str
        type bank:List[str]
        returntype:int
        """
        bank = set(bank)
        if end not in bank:
            return -1
        
        change_map = {
            "A":"CGT",
            "C":"AGT",
            "G":"CAT",
            "T":"CGA",
        }
        queue = [(start,0)]
        while queue:
            node,step = queue.pop(0)

            if node == end:
                return step
            for i , s in enumerate(node):
                for c in change_map[s]:
                    new = node[:i] + c + node[i+1:]
                    if new in bank:
                        queue.append((new,step+1))
                        bank.remove(new)
        return -1
# @lc code=end

