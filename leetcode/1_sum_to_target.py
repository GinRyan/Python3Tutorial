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
