class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        
        for num in nums:
            length = 1

            if num-1 not in nums:
                while num+length in nums:
                    length += 1

            max_length = max(max_length, length)            

        return max_length