class Node:
    def __init__(self):
        self.children = {}
        self.word = False
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        answer = []
        self.num_words = len(words)
        trie = Node()
        
        for word in words:
            current = trie
            
            for char in word:
                if char not in current.children:
                    current.children[char] =  Node()
                current = current.children[char]
            current.word = True
        
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                self.dfs(i, j, board, trie, answer, "")
                
        return answer
    
    def dfs(self, i, j, board, trie, answer, word):
        
        if self.num_words == 0: 
            return
        
        if trie.word:
            self.num_words -=1
            answer.append(word)
            trie.word = False
            
        if j<0 or i<0 or j>=len(board[0]) or i>=len(board):
            return
        
        if board[i][j] not in trie.children:
            return
        
        temp = board[i][j]
        board[i][j] = " "
        
        self.dfs(i+1, j, board, trie.children[temp], answer, word + temp)
        self.dfs(i-1, j, board, trie.children[temp], answer, word + temp)
        self.dfs(i, j+1, board, trie.children[temp], answer, word + temp)
        self.dfs(i, j-1, board, trie.children[temp], answer, word + temp)
        
        board[i][j] = temp