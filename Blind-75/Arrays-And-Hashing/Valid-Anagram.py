class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def idx(c) -> int:
            return ord(c) - ord('a')

        freqs = [0]*26
        freqt = [0]*26
        for c in s:
            freqs[idx(c)] += 1
        for c in t:
            freqt[idx(c)] += 1

        return freqs == freqt
