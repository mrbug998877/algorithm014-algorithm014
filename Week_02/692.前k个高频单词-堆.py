#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import collections, heapq
        Freqs = collections.Counter(words)
        return heapq.nsmallest(k, Freqs,
            key=lambda word:(-Freqs[word], word))

# @lc code=end

