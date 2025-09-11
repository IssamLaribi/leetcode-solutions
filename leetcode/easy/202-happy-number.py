class Solution:
    def isHappy(self, n: int) -> bool:

        new_number = 0
        temp = n
        seen = [n]

        while True:
            while temp > 0:
                new_number += (temp % 10) ** 2
                temp = temp // 10
            
            
            
            if new_number == 1:
                return True
            elif new_number in seen:
                return False
            
            seen.append(new_number)
            temp = new_number
            new_number = 0
