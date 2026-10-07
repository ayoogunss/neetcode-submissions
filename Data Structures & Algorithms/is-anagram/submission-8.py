class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        an1 = {}
        an2 = {}
        for i in s:
            if i not in an1:
                an1[i] = 1
            else:
                an1[i] += 1
        for i in t:
            if i not in an2:
                an2[i] = 1
            else:
                an2[i] += 1
        return an1 == an2