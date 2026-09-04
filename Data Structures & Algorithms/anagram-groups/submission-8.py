class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}  # act:[act, cat]
        for s in strs:
            content = "".join(sorted(s))
            if content in hashTable:
                hashTable[content].append(s)
            else:
                hashTable[content] = [s]
        return list(hashTable.values())