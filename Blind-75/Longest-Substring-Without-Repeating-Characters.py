class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        l= deque()
        for right in range(len(s)):
            while s[right] in l:
                l.popleft()
                left += 1

            l.append(s[right])
            maxLen = max(maxLen, len(l))

        return maxLen
