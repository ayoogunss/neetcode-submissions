class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dups = defaultdict(int)
        freq = []
        for i in nums:
            dups[i] += 1
        for i in range(k):
            max = 0
            for j in dups:
                if dups[j] > max:
                    max = dups[j] # store the value to compare
                    s = j # store key to append
            freq.append(s)
            del dups[s] 
        return freq
