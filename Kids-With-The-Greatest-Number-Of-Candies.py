class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ans = []
        for candy in candies:
            ans.append(candy + extraCandies >= maxCandies)

        return ans
