class Solution:
    def helperDFS(self,v,visited,stack,nodes):
        visited[v] = 1
        
        if v in nodes:
            for i in nodes[v]: 
                if visited[i] == 0: 
                    self.helperDFS(i,visited,stack,nodes)
                elif visited[i] == 1:
                    return
        
        visited[v] = 2
        stack.insert(0,v)
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes = {}
        degrees = [0]*numCourses
        visited = []
        
        for edge in prerequisites:
            if edge[1] not in nodes:
                nodes[edge[1]] = [edge[0]]
            else:
                nodes[edge[1]].append(edge[0])
                
        visited = [0]*numCourses 
        stack =[] 
        
        for i in range(numCourses): 
            if visited[i] == 0: 
                self.helperDFS(i,visited,stack,nodes) 
                
        if len(stack)<numCourses:
            return []
        else:
            return stack