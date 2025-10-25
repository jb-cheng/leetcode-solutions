class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Create arrays that store the frequencies of each letter
        s1Frequencies, s2Frequencies = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Frequencies[ord(s1[i]) - ord('a')] += 1
            s2Frequencies[ord(s2[i]) - ord('a')] += 1

        # Initial check for matches
        matches = 0
        for i in range(26):
            matches += (1 if s1Frequencies[i] == s2Frequencies[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            letter = ord(s2[r]) - ord('a')
            s2Frequencies[letter] += 1
            if s1Frequencies[letter] == s2Frequencies[letter]:
                matches += 1
            elif s1Frequencies[letter] + 1 == s2Frequencies[letter]:
                matches -= 1

            letter = ord(s2[l]) - ord('a')
            s2Frequencies[letter] -= 1
            if s1Frequencies[letter] == s2Frequencies[letter]:
                matches += 1
            elif s1Frequencies[letter] - 1 == s2Frequencies[letter]:
                matches -= 1
                
            l += 1

        return matches == 26