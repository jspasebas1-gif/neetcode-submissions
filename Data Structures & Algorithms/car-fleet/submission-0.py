class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

            
        # Pair position and speed, then sort by position (descending)
        cars = sorted(zip(position, speed), reverse=True)

        fleets = []
        for pos, spd in cars:
            time = (target - pos) / spd
            # If the current car's time is greater than the last fleet's time,
            # it forms a new fleet.
            if not fleets or time > fleets[-1]:
                fleets.append(time)

        return len(fleets)



            