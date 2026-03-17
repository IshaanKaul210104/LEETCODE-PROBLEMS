class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        count, maxCount = 0, 0
        for num in nums:
            if num - 1 not in seen:
                temp = num
                while temp in seen:
                    count += 1
                    temp += 1
            maxCount = max(maxCount, count)
            count = 0
        return maxCount
