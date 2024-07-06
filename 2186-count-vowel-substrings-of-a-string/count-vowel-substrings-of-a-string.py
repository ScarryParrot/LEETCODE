class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        
        for i in range(len(word)):
            if word[i] in vowels:
                vowel_set = set()
                for j in range(i, len(word)):
                    if word[j] in vowels:
                        vowel_set.add(word[j])
                        if len(vowel_set) == 5:
                            count += 1
                    else:
                        break
                        
        return count