class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenght = len(nums)
        hashSet = set()
        for i in range(lenght):
            if nums[i] in hashSet:
                return True
            hashSet.add(nums[i])
        return False