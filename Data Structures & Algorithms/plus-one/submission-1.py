class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        # concatenate the list into a string
        for i in digits:
            num += str(i)
        # turn string into an integer then add the 1
        num = int(num)
        num += 1
        # turn it back to a string then into a list
        num = str(num)
        num = list(num)
        # traverse the list then turn each character back into an integer
        for i in num:
            i = int(i)
        return num