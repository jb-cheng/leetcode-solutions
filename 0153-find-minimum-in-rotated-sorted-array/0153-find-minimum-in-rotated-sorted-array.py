class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val: int = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:           
            mid = (l + r) // 2
            min_val = min(min_val, nums[mid])
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1

        return min_val