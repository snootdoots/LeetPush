class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [gain[0]]
        for i in range(1, len(gain)):
            prefix.append(prefix[i-1] + gain[i])
        
        mymax = 0
        for i in prefix:
            mymax = max(mymax, i)
        return mymax