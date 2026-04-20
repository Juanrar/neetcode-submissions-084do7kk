class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #analisar toda la lista
            # guardar el conteo de apariciones
            # compararlos y devolver el mayor
                # tener guardado el mayor
        count = {}
        best, bestCount = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n,0)
            best = n  if count[n] > bestCount else best
            bestCount = max(count[n], bestCount)

        return best