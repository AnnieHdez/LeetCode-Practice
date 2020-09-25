class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                visited = [[False] * m for i in range(n)]
                if board[i][j]==word[0]:
                    if self.recursive(board, word,i,j,n,m,visited):
                        return True
                        
        return False
    
    def recursive(self,board, word,i,j,n,m,visited):
        if len(word) == 0:
            return True
        
        if i<0 or i>=n or j<0 or j>=m:
            return False
        
        if visited[i][j] or board[i][j]!=word[0]:
            return False
        
        visited[i][j]=True
        answer= self.recursive(board, word[1:],i+1,j,n,m,visited) or self.recursive(board, word[1:],i-1,j,n,m,visited) or self.recursive(board, word[1:],i,j+1,n,m,visited) or self.recursive(board, word[1:],i,j-1,n,m,visited) 
        visited[i][j]=False
        return answer