class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        return a == a[::-1]
