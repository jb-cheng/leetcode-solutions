class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val: int = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # Fully sorted
            if nums[l] < nums[r]:
                min_val = min(min_val, nums[l])
                break
            
            m = (l + r) // 2
            min_val = min(min_val, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return min_val