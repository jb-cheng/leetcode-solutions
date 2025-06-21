class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed: int = r

        while l <= r:
            speed: int = (l + r) // 2

            eating_time: int = 0
            for pile in piles:
                eating_time += math.ceil(pile/speed)

            if eating_time > h:
                l = speed + 1
            else:
                r = speed - 1
                min_speed = speed

        return min_speed