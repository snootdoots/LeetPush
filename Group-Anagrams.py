class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        returnList = []
        for s in strs:
            curr = "".join(sorted(list(s)))
            if curr in mydict:
                returnList[mydict[curr]].append(s)
            else:
                mydict[curr] = len(returnList)
                returnList.append([s])
        return returnList
