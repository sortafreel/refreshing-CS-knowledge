from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set()
        nums_dict = {}
        for i, value in enumerate(nums):
            if target - value in nums_set:
                return [i, nums_dict[target - value]]
            else:
                nums_set.add(value)
                nums_dict[value] = i


# nums = [2, 7, 11, 15]
# target = 9
# nums = [3, 3]
# target = 6
nums = [-1, -2, -3, -4, -5]
target = -8

sol = Solution()
print(sol.twoSum(nums, target))
