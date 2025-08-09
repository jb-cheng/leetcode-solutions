class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Since every number is in ascending order except the subracting cases, 
        # reverse s, and if s[i] < s[i-1], then subtract s[i]
        num = 0
        previous = 0
        for char in reversed(s):
            current = roman2int[char]
            if current >= previous:
                num += current
            else:
                num -= current
            previous = current

        return num