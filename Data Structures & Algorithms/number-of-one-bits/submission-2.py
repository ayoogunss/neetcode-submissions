class Solution:
    def hammingWeight(self, n: int) -> int:
        stored = []
        count = 0
        for i in range(32):
            stored.append("0")
        for i in range(32):
            if 2 ** (31-i) <= n:
                stored[i] = "1"
                n -= 2** (31-i)
        for i in range(len(stored)):
            if stored[i] == "1":
                count += 1
        return count
        