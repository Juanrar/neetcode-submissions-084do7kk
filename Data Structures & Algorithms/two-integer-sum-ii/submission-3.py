class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while r > l:
            currentSum = numbers[l] + numbers[r]
            if currentSum == target:
                return [l+1, r+1]
            elif currentSum > target:
                r -=1
            else:
                l += 1
        return []