class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest: int = 0

        l: int = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])

            longest = max(longest, r-l+1)

        return longest