class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = {}
        for i in range(0, len(s)):
            if s[i] in frequency:
                frequency[s[i]] += 1
            else:
                frequency[s[i]] = 1

        for i in range(0, len(s)):
            if frequency[s[i]] == 1:
                return i
                
        return -1