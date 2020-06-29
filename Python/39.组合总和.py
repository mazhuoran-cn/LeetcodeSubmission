#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def a(i, combine, target):
            summation = sum(combine)
            if summation == target:
                res.append(combine)
            for j, candidate in enumerate(candidates[i:]):
                if not summation + candidate > target:
                    a(i+j, [*combine, candidate], target)

        for i, candidate in enumerate(candidates):
            a(i, [candidate], target)

        return res
        

