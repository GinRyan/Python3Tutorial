"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []

        counts = len(nums)
        print(nums)

        indexBase = 0
        indexDiff = 1

        while indexBase < counts:
            diffVal = target - nums[indexBase]
            indexDiff = indexBase + 1
            while indexDiff < counts:
                if diffVal == nums[indexDiff]:
                    ret.append(indexBase)
                    ret.append(indexDiff)
                    return ret
                indexDiff += 1
            indexBase +=1
     
        return ret


print(Solution().twoSum([7, 2, 11, 15, 4], 6))
