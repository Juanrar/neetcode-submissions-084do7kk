class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = dict()
        hashT = dict()

        for word in s:
            if word in hashS:
                hashS[word] += 1
            else:
                hashS[word] = 0

        for word in t:
            if word in hashT:
                hashT[word] += 1
            else:
                hashT[word] = 0
    
        return True if hashS == hashT else False