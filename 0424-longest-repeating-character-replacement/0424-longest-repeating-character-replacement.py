class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest: int = 0
        frequencies = dict()

        l = 0
        for r in range(len(s)):
            frequencies[s[r]] = 1 + frequencies.get(s[r], 0)
            
            while (r-l+1) - max(frequencies.values()) > k:
                frequencies[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)

        return longest