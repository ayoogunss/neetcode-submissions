class Solution:
    def countBits(self, n: int) -> List[int]:
        bitcount = []
        for i in range(n+1):
            num = i
            count = 0
            bits = ["0"] * 10
            for j in range(10):
                if 2 ** (9-j) <= num:
                    bits[j] = "1"
                    num -= 2 ** (9-j)
            for j in range(10):
                if bits[j] == "1":
                    count += 1
            bitcount.append(count)
        return bitcount
