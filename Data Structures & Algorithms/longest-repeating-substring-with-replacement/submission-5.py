class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        l = 0
        charHash = {}

        maxf = 0
        for r in range(len(s)): 
            charHash[s[r]] = 1 + charHash.get(s[r], 0)
            maxf = max(maxf, charHash[s[r]])

            while((r-l + 1) - maxf > k):
                charHash[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result
            
        