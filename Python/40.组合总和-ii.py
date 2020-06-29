#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def a(i, combine, target):
            summation = sum(combine)
            if summation == target:
                if sorted(combine) not in res:
                    res.append(sorted(combine))
            for j, candidate in enumerate(candidates[i+1:]):
                if not summation + candidate > target:
                    a(i+j+1, [*combine, candidate], target)

        for i, candidate in enumerate(candidates):
            a(i, [candidate], target)

        return res

