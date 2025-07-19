class NumArray:
    def __init__(self, nums: List[int]):
        self.cumulative_sums = []
        total = 0
        for num in nums:
            total += num
            self.cumulative_sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.cumulative_sums[right]
        else:
            return self.cumulative_sums[right] - self.cumulative_sums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)