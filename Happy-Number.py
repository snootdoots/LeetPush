class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)

        while int(s) > 10:
            total = 0
            for c in s:
                total += int(c) ** 2
            s = str(total)
        
        if int(s) in [1, 7, 10]:
            return True
        else:
            return False