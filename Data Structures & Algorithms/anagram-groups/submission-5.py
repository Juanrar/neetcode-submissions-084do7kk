class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            hashMap = defaultdict(list) # charactes: anagram
            for anagram in strs:
                characters = "".join(sorted(anagram))
                #print(characters)
                hashMap[characters].append(anagram)

            return hashMap.values()