class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # access key that don't exist, create the ley by default
        res = defaultdict(list) 
        for i in strs:
            # sort the string then convert back to string
            sortedi = ''.join(sorted(i)) 
            # add the string to it's respective anagram key
            res[sortedi].append(i)
        return list(res.values())
    