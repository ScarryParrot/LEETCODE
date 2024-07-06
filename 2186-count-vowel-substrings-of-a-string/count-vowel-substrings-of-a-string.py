class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v={'a','e','i','o','u'}
        c=0
        for i in range(len(word)):
            if word[i] in v:
                v_set=set()
                for j in range(i,len(word)):
                    if word[j] in v:
                        v_set.add(word[j])
                        if len(v_set) == 5:
                            c+=1
                    else:
                            break
        return c