class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1  
        INT_MIN = -2**31    

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while (temp << 1) <= dividend:
                temp = temp << 1
                multiple = multiple << 1

            dividend = dividend - temp
            quotient = quotient + multiple

        if negative:
            quotient *= -1 

        def clamp(x, low, high):
            return max(low, min(x, high))
            
        return clamp(quotient, INT_MIN, INT_MAX)
        
