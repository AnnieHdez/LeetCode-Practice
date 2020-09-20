class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
               return self.helper(0, s, set(wordDict), {})

    def helper(self, k, s, wordDict, cache):
        if k == len(s):
            return []
        elif k in cache:
            return cache[k]
        else:
            cache[k] = []
            for i in range(k, len(s)):
                left = s[k:i+1]
                if left in wordDict:
                    remainder = self.helper(i+1, s, wordDict, cache)
                    if remainder:
                        for x in remainder:
                            cache[k].append(left + " " + x)
                    elif (i == len(s)-1):
                        cache[k].append(left)
            return cache[k]