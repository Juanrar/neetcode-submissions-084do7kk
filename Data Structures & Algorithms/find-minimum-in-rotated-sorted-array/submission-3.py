class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float('inf')
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            print("brecha: ", nums[l], nums[mid], nums[r])

            #saber si esta rotado
            if nums[l] > nums[r]:
                result = min(result, nums[r])
                r -= 1
                if nums[l] < nums[r]:
                    return result
            
            elif nums[mid] < nums[r]:
                result = min(result, nums[mid])
                r = mid - 1

            else:
                result = min(result, nums[l])
                l = mid + 1
        return result