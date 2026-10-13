class Solution:
    def reverseBits(self, n: int) -> int:
        num = [(n >> i) &1  for i in range(31,-1,-1)]
        num = num[::-1]
        number = 0
        for i in range(32):
            if(num[i] == 1):
                number += 2** (31-i)

        return number