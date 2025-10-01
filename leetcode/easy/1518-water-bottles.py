class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles   # count bottles you drink
        empty = numBottles   # empty bottles after drinking them
        
        while empty >= numExchange:
            new_full = empty // numExchange       # how many new bottles we can get
            total += new_full                     # drink them
            empty = empty % numExchange + new_full  # leftover empty + new empty after drinking
        
        return total
