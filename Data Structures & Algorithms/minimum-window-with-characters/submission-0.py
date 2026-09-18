class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return

        #hashmaps para llevar los contadores,
        #se utilizan para saber si efectivamente tengo todos las
        #letras de t
        countT, window = {}, {}

        #rellenamos el hashmap con los valores que quiero buscar
        for c in t:
            countT[c] = 1 + countT.get(c,0)

        #Contamos los que tengo y los que faltal 
        have, need = 0, len(countT)    
        #variables para guardar los resultados en la recorrida
        res, resLen= [-1,-1], float("infinity")

        l=0
        for r in range(len(s)):
            c=s[r]
            #vamos guardando las letras y luego las comparamos es la que bucamos
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                #actualizamos el posible resultado
                if (r - l + 1) < resLen:
                    res=[l,r]
                    resLen = (r-l+1)
                #sacando valores de la ventana
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1
                l+=1
        l,r= res
        return s[l:r+1] if resLen != float("inf") else ""






