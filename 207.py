import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        print graph
        print visit

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            print i,'i'
            return True

        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True

sl=Solution()
n=4
p=[[1,0],[2,3],[3,1],[3,0]]
print sl.canFinish(n,p)

