class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        car_fleet = zip(position, speed)
        car_fleet = sorted(car_fleet, key=lambda x: x[0], reverse=True)
        stack = []

        for car in car_fleet:
            position, speed = car
            arrival = (target - position) / speed    
            if not stack or arrival > stack[-1]:
                stack.append(arrival)

        return len(stack)


        