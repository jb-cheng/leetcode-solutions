class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}

        # Create cumulative sum
        cumulative_sum = []
        total = 0
        for word in words:
            if word[0] in VOWELS and word[-1] in VOWELS:
                total += 1
            cumulative_sum.append(total)


        numVowels = []
        for query in queries:
            left, right = query[0], query[1]
            if left == 0:
                numVowels.append(cumulative_sum[right])
            else:
                numVowels.append(cumulative_sum[right] - cumulative_sum[left-1])

        return numVowels