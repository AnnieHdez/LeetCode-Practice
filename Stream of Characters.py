class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for word in words:
            self.trie.insert(word[::-1])
            
        self.queries = deque()

    def query(self, letter: str) -> bool:
        self.queries.appendleft(letter)
        current = self.trie.root['$']
        
        for let in self.queries:
            if let in current:
                current = current[let]
                if '#' in current:
                    return True
            else:
                break
        return False

        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
class Trie:
    root = {}
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root['$']={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current =  self.root['$']
        for letter in word:
            if letter in current:
                current = current[letter]
            else:
                current[letter]={}
                current = current[letter]
        current['#']={}  