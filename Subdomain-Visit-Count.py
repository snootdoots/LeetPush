class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        myset = defaultdict(int)
        for domain in cpdomains:
            count, website = domain.split()
            subdomains = website.split('.')
            for i in range(len(subdomains)):
                curr = ".".join(subdomains[i:len(subdomains)])
                myset[curr] += int(count)
        return_arr = []
        for i in myset:
            return_arr.append(f"{myset[i]} {i}")
        return return_arr