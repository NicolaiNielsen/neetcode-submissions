class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = list(zip(speed, position))
        fleet.sort(key=lambda x: x[1], reverse=True)
        
        for speed, pos in fleet:
            arrival_time = (target - pos) / speed

            if stack and stack[-1] < arrival_time:
                stack.append(arrival_time)
            
            if not stack:
                stack.append(arrival_time)

        return len(stack)

