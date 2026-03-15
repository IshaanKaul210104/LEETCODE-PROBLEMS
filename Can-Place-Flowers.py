class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if (len(flowerbed) == 1 and flowerbed[0] == 0) or (len(flowerbed) == 2 and flowerbed[0] == 0 and flowerbed[1] == 0):
            return 1 >= n
        if len(flowerbed) == 3 and flowerbed[0] == 0 and flowerbed[1] == 0 and flowerbed[2] == 0:
            return 2 >= n
        count: int = 0
        i: int = 0
        if i == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1
            flowerbed[0] = -1
        while i < (len(flowerbed) - 2):
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i + 2] == 0:
                flowerbed[i] = -1
                count += 1
                i += 1
            i += 1
        if i == len(flowerbed) - 2 and flowerbed[-2] == 0 and flowerbed[-1] == 0 and flowerbed[-3] != -1:
            count += 1
        return count >= n
