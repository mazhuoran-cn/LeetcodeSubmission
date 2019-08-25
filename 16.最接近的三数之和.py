#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        save = dict()
        for i, n1 in enumerate(nums):
            for n2 in nums[i+1:]:
                if n1, n2 
                ideal = target - n1 - n2
                if ideal in nums[i+2:]:
                    return target
                else:
                    cmp_res = [abs(ideal - a) for a in nums[i+2]]
                    n3 = nums[cmp_res.index(min(cmp_res))+i+2]
                    save[(n1, n2, n3)] = abs
        return 
                

