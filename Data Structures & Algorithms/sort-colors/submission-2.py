class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0,0,0]

        for n in nums:
            count[n] += 1 
            print("valor de n:", n)
            print("cuenta: ",count)
        
        print(count)

        j = 0
        for i in range(len(count)):
            for n in range(count[i]):
                nums[j] = i
                j += 1
            print(nums)
        