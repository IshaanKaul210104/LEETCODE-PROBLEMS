class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = [0]*(len(nums) + 1)
        for num in nums:
            freq[num] += 1
        fir, sec = -1, -1
        for i in range(1, len(nums) + 1):
            if freq[i] == 2:
                fir = i
            elif freq[i] == 0:
                sec = i
        return [fir, sec]
