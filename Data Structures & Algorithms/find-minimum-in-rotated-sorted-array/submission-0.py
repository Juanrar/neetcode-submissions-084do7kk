class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float('inf')
        for n in nums:
            result = min(result, n)
        
        return result