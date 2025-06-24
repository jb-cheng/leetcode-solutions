class TimeMap:
    
    def __init__(self):
        self.vals: dict[str, list[str, int]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals: list = self.vals[key]
        res: str = ""
        l, r = 0, len(vals) - 1

        while l <= r:
            mid: int = (l + r) // 2

            if vals[mid][1] == timestamp:
                return vals[mid][0]
            elif vals[mid][1] < timestamp:
                res = vals[mid][0]

            if timestamp > vals[mid][1]:
                l = mid + 1
            else:
                r = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)