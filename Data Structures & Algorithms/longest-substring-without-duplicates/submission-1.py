class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        substring = set()
        l = 0

        for r in range(len(s)):
            #print(s[r], substring)
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            result = max(result, r - l + 1)
        
        return result
