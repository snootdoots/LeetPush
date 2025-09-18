class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for s in timePoints:
            tensH = int(s[0])
            onesH = int(s[1])
            tensM = int(s[3])
            onesM = int(s[4])
            my_min = onesM + 10*tensM + 60*onesH + 600*tensH
            minutes.append(my_min)
        minutes = sorted(minutes)
        minutes.append(minutes[0] + 1440)
        smallest = 1440
        for i in range(len(minutes) - 1):
            diff = minutes[i+1] - minutes[i]
            smallest = min(smallest, diff)
        return smallest