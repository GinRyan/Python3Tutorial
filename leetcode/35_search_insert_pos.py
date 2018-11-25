"""给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2

示例 2:

输入: [1,3,5,6], 2
输出: 1

示例 3:

输入: [1,3,5,6], 7
输出: 4

示例 4:

输入: [1,3,5,6], 0
输出: 0

"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        target_pos = 0
        counts = len(nums)
        if counts == 1:
            if target > nums[0]:
                return 1
            elif target <= nums[0]:
                return 0
        for index_, item_ in enumerate(nums):
            # print("%d: %d" % (index_, item_))
            if index_ == 0:  # 首位置
                if target == item_:
                    target_pos = index_
                    print("存在值，首位取值")
                    return target_pos
                if target < item_:
                    target_pos = index_
                    print("无存在值，首位插入")
                    return target_pos
                if target > item_ and target < nums[index_ + 1]:
                    target_pos = index_ + 1
                    print("无存在值，中间插入")
                    return target_pos
            elif index_ == counts - 1:  # 末位置
                if target == item_:
                    target_pos = index_
                    print("存在值，末尾取值")
                    return target_pos
                if target > item_:
                    target_pos = index_ + 1
                    print("无存在值，末尾插入")
                    return target_pos
            else:
                if target == item_:
                    target_pos = index_
                    print("存在值，中间取值")
                    return index_
                if target > item_ and target < nums[index_ + 1]:
                    target_pos = index_ + 1
                    print("无存在值，中间插入")
                    return target_pos
        return target_pos


print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 7))
print(Solution().searchInsert([1, 3, 5, 6], 0))
print(Solution().searchInsert([1, 3, 4, 6], 5))
print(Solution().searchInsert([1], 2))
