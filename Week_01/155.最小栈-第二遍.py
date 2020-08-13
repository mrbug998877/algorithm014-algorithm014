#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
#        self.minstack =[math.inf]
        
    def push(self, x):
        self.stack.append(x)
#        self.minstack.append(min(x, self.minstack[-1]))
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return min(self.stack)





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

