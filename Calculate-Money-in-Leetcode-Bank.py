class Solution:
    def totalMoney(self, n: int) -> int:
        # 1 2 3 4 5 6 7 -> 28
        # 2 3 4 5 6 7 8 -> 28 + 7 = 35
        # 3 4 5 6 7 8 9 -> 28 + 14 = 42
        weeks = n // 7 # number of weeks
        days = n % 7 # number of days
        print(weeks*28, sum(range(weeks))*7, sum(range(days+1)), weeks*days)
        return weeks*28 + sum(range(weeks))*7 + sum(range(days+1)) + weeks*days