class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empties = numBottles
        
        while empties >= numExchange:
            # Exchange empties for 1 full
            empties -= numExchange
            numExchange += 1  # Next exchange cost increases
            # Drink the new bottle
            drank += 1
            empties += 1
        
        return drank
