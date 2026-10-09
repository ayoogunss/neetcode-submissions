class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        seen = set()
        sum = 0
        i = 0
        while True:
            sum += int(num[i]) ** 2
            if i == len(num) - 1:
                if sum == 1:
                    return True
                if sum in seen:
                    return False
                seen.add(sum)
                num = str(sum)
                i = 0
                sum = 0
                continue
            i += 1
        return False