class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3

        for n in nums:
            count[n] += 1 

        
        print(count)

        j = 0
        for i in range(len(count)):
            for n in range(count[i]):
                nums[j] = i
                j += 1
        