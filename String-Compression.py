class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        i = 0
        while i < len(chars):
            char = chars[i]
            freq = 0
            while i < len(chars) and chars[i] == char:
                freq += 1
                i += 1
            ans.append(char)
            if freq > 1:
                ans.extend(list(str(freq)))
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)
