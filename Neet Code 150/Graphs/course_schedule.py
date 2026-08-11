from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        # first create the adjecency list
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses # creating the indegree array
        topo = []

        # populating our adjacency list and indegree array
        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue: 
            curr = queue.popleft()
            topo.append(curr)

            for next_course in adj[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(topo) == numCourses

def main():
    n = 3
    prerequisites = [[1,0],[2,0]]
    result = Solution()
    print(result.canFinish(n,prerequisites))

if __name__ == "__main__":
    main()


        