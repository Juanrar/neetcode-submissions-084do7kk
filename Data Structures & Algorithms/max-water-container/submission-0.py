class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Cuenta para calcular el area el area es (distancia * (altura minima))
        result = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l],heights[r])
            #print("area: ", area)
            result =  max(result, area)
            #print("result: ", result)
            if heights[l] > heights[r]:
                r -= 1
            else: # heights[l] < heights[r]
                l += 1
        
        return result