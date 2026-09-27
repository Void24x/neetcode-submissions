class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList: return 0

        n = len(wordList) +1

        vis  = {}

        vis[beginWord] = False
        for e in wordList:
            vis[e] = False

        q = deque()

        q.append((beginWord, 1))
        ans =  0
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(0, len(word)):
                init = 'a'
                for j in range(0,26):
                    chars = list(word)
                    chars[i] = chr(ord('a') + j)
                    nxtW = ''.join(chars)
                    if nxtW in wordList and not vis[nxtW]:
                            vis[nxtW] = True
                            q.append((nxtW, steps+1))
        return 0
                    
                    
            


        