class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # tener un hashmap con clave sort y el valor los strs
        # 'act': [act, cat]
        result = {}
        for s in strs:
            anagram = ''.join(sorted(s))
            if anagram in result:
                result[anagram].append(s)
            else:
                result[anagram] = [s]
        
        return list(result.values())