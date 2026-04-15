class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        #iterando uno por uno
            #analisar que letras tienen
            #guardar esas letras y compararlas con otras palabras
        
        for s in strs:
            lista = []
            for i in range(len(s)):
                lista.append(s[i])
            lista.sort()
            agrupado= ''.join(lista)
            if agrupado not in result:
                result[agrupado] = []
            result.get(agrupado, []).append(s)
            
        return list(result.values())