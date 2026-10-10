class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dup = defaultdict(int)
        for i in nums:
            dup[i] += 1
        for i in dup:
            if dup[i] == 1:
                return i
        return 0