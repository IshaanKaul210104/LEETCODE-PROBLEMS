class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)

        def isVowel(c) -> bool:
            return c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        vowels = []
        l = list(s)

        for i in range(n):
            if isVowel(l[i]):
                vowels.append(l[i])

        k = 0
        for i in range(n - 1, -1, -1):
            if isVowel(l[i]):
                l[i] = vowels[k]
                k += 1

        return ''.join(l)
