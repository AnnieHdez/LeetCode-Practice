class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
            
        for char in word:
            if char not in current.children:
                current.children[char] =  Node()
            current = current.children[char]
        current.word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.Rsearch(word, self.root)
        
    def Rsearch(self, word: str, trie) -> bool:
        if word=="":
            if trie.word:
                return True
            else:
                return False
        elif word[0] == '.':
            answer = False
            for element in trie.children:
                a = self.Rsearch(word[1:], trie.children[element])
                answer = answer or a
            return answer
        elif word[0] not in trie.children:
            return False
        
        else:
            return self.Rsearch(word[1:], trie.children[word[0]])
        return True
            

class Node:
    def __init__(self):
        self.children = {}
        self.word = False