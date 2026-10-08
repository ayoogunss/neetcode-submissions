class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = set(nums)
        for i in range(max(nums)):
            if i not in check:
                return i
        return max(nums) + 1