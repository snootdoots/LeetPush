class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [[] for _ in range(target+1)]
        for candidate in candidates:
            if candidate <= target:
                res[candidate].append([candidate])

            for i in range(candidate+1, target+1):
                for arr in res[i-candidate]:
                    new_arr = arr + [candidate]
                    res[i].append(new_arr)
        return res[target]