class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # number : count
        freq = [[] for i in range(len(nums)+1)]
        #list de frecuencias-> Lista[frecuencia]=numero
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        #print("Hashmap con los contadores: ",count)
        for num, count in count.items():
            freq[count].append(num)
        #print("Lista de frecuentes: ", freq)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                #print("lista del resultado: ", res)
                if len(res) == k:
                    return res


