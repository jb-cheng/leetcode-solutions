class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()

        for i, num in enumerate(nums):
            if target - num in numbers:
                return [i, numbers[target - num]]
            else:
                numbers[num] = i