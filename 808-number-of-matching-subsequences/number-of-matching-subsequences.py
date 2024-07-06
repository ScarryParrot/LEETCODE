class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict = {}
        c = 0
        
        def helper(word):
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)

        for w in words:
            if w in dict:
                if dict[w]:
                    c += 1
            else:
                is_subseq = helper(w)
                dict[w] = is_subseq
                if is_subseq:
                    c += 1
        
        return c