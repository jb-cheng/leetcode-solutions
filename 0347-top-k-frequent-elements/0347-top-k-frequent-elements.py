class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        return [frequency[0] for frequency in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)][:k]

