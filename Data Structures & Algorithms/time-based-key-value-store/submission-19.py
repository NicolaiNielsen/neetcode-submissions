class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            #find maximum value

            l = 0
            r = len(self.map[key]) - 1
            array = self.map[key]
            res = ""
            while l <= r:
                #t = 4, [1, 2, 3, 4, 4, 5]
                m = (l + r) // 2

                if array[m][1] <= timestamp:
                    res = array[m][0]
                    l = m + 1
                else:
                    r = m - 1

            return res