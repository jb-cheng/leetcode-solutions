class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary Search
        left = 0
        right = x
        predecessor = 0    # Stores the largest number whose square is smaller than x so far

        while left <= right:
            midpoint = left + (right - left) // 2
            if midpoint*midpoint > x:
                right = midpoint - 1
            elif midpoint*midpoint < x:
                # If m*m is less than x, the left bound and midpoint will always shift right
                left = midpoint + 1
                predecessor = midpoint
            else:
                return midpoint
        return predecessor