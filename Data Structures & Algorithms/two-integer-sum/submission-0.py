class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        findSum = {}
        for idx, i in enumerate(nums):
            needed = target - i;
            if needed not in findSum:
                findSum[i] = idx
            else:
                return [findSum[needed], idx]
        return []