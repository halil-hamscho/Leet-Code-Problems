'''
There are a total of numCourses courses you have to take, 
labeled from 0 to numCourses - 1
You are given an array 
prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai firt

For example = [0, 1] indicates that to take
course 0 you have tof irst take course 1

Return the ordering of courses you should
take to finish all courses. If there are 
many valid answers, return any of them
If it is impossible to finish all courses, return
an empty array

Steps:
1. First Create the adjacency list
2. Have two sets, the visited and the cycle
    the visited gets updated after we check if the current index in the
    adjacency list has a cycle by running dfs on it's prereqs

'''

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # First create the adjacency list
        # Will use a dictionary
        # index is the course number
        prereq = { course:[] for course in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # answer
        topo = []
        # utily sets
        visited, cycle = set(), set()
        # cycle will be updated
        # we will start with the first number
        def dfs(crs):
            # it is currently in the dfs search
            if crs in cycle:
                return False
            # skip revisit
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                # if it is in cycle
                if dfs(pre) == False:
                    return False
            # after going through every single prereq
            cycle.remove(crs)
            # after we remove from cycle, we add to visit
            visited.add(crs)
            topo.append(crs)
            return True
        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return topo



