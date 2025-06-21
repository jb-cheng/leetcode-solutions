class Solution:
    def findMin(self, nums: List[int]) -> int:        
        l, r = 0, len(nums) - 1
        pivot: int = nums[0]
        min_num: int = math.inf

        mid: int = 0
        while l <= r:
            mid = (l + r) // 2
            min_num = min(min_num, nums[mid], nums[l], nums[r])

            if nums[mid] > pivot:
                l = mid + 1
            else:
                r = mid - 1

        return min_num