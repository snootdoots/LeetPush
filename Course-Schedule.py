class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use topological sort
        queue = []
        adj_list = [[] for i in range(numCourses)]
        indegree = defaultdict(int)

        # set up everything
        for i in prerequisites:
            req, crs = i[0], i[1]
            adj_list[req].append(crs)
            indegree[crs] += 1
        
        # iterate through queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # while through queue
        count = 0
        while queue:
            curr = queue.pop(0)
            count += 1
            for i in adj_list[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
    
        return count == numCourses