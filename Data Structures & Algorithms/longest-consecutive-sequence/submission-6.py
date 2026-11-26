class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_sort = sorted(nums)
        counts = {}
        max_count = 0
        for n in nums_sort:
            previus = n - 1
            counts[n] = 1 + counts.get(previus, 0 )
            max_count = max(max_count, counts[n])
        #print(counts)
        return max_count
