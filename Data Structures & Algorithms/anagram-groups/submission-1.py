class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for i in strs:
        #     # what are we concatenating on this line? 
        #     sortedi = ''.join(sorted(i))
        #     res[sortedi].append(i)
        # return list(res.values())
        res = {}
        for i in strs:
            sortedi = ''.join(sorted(i))
            if sortedi not in res:
                res[sortedi] = []
                res[sortedi].append(i)
            else:
                res[sortedi].append(i)
        return list(res.values())