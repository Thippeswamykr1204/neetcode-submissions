class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            sortedi = ''.join(sorted(i))
            hashmap[sortedi].append(i)
        return list(hashmap.values())

        
        