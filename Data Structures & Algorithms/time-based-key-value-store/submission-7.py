class TimeMap:

    def __init__(self):
        self.map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([timestamp, value])
        else:
            self.map[key] = [[timestamp, value]]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        l = 0
        r = len(self.map[key]) - 1
        res = ""
        while l <= r:
            m = (r + l) // 2


                
                
            if timestamp >= self.map[key][m][0]:
                l = m + 1
                res = self.map[key][m][1]
            else:
                r = m - 1

        return res



        
