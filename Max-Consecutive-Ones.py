class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count, maxcount = 0, 0
        while i < len(nums):
            if nums[i] == 1:
                while i < len(nums) and nums[i] == 1:
                    count += 1
                    i += 1
                maxcount = max(maxcount, count)
            i += 1
            count = 0
        return maxcount
