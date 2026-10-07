class Solution:
    def isValid(self, s: str) -> bool:
        paren = []

        for i in s:
            if i == "(":
                paren.append(i)
            elif i == "[":
                paren.append(i)
            elif i == "{":
                paren.append(i)
            elif len(paren) == 0:
                return False
            elif i == ")":
                if paren[-1] != "(":
                    return False
                paren.pop()
            elif i == "]":
                if paren[-1] != "[":
                    return False
                paren.pop()
            elif i == "}":
                if paren[-1] != "{":
                    return False
                paren.pop()
        return len(paren) == 0