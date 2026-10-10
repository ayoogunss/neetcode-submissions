class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # use dictionary
        dup = defaultdict(int)
        for i in nums:
        # pair num key with number of occurences
            dup[i] += 1
        for i in dup:
            #if a number appears once when return it
            if dup[i] == 1:
                return i
        return 0