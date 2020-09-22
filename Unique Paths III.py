class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        x=0
        y=0
        self.answer = 0
        empty = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] != -1:
                    empty+=1
        
        self.backTrack(grid, x, y, empty-1) 
        return self.answer
        
        
    def backTrack(self, grid, x, y, rest): 
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or  grid[x][y] < 0: 
            return
        
        if grid[x][y]==2 and rest == 0:
            self.answer+=1
        
        temp = grid[x][y]
        
        grid[x][y]=-2
        self.backTrack(grid, x+1, y, rest-1)
        grid[x][y]= temp

        grid[x][y]=-2
        self.backTrack(grid, x-1, y, rest-1)
        grid[x][y]= temp

        grid[x][y]=-2
        self.backTrack(grid, x, y+1, rest-1)
        grid[x][y]= temp

        grid[x][y]=-2
        self.backTrack(grid, x, y-1, rest-1)
        grid[x][y]= temp
            
        return 