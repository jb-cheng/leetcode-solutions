class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        valid_indices = range(len(nums))

        # Add a "buffer" for the ends of the array
        left_prod = nums.copy() + [1]
        right_prod = nums.copy() + [1]

        # Cumulative product L -> R
        for i in valid_indices:
            left_prod[i] = left_prod[i-1] * left_prod[i]

        # Cumulative product R -> L
        for i in reversed(valid_indices):
            right_prod[i] = right_prod[i+1] * right_prod[i]

        # product except self of `i` is left_prod * right_prod up to `i`.
        return [left_prod[i-1] * right_prod[i+1] for i in valid_indices]