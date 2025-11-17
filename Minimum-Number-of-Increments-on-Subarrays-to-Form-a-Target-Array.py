class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        diff = [target[0]]
        for i in range(1, len(target)):
            diff.append(target[i] - target[i-1])
        mysum = 0
        for i in diff:
            if i > 0:
                mysum += i
        return mysum