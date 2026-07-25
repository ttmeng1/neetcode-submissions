class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for s in strs:
            if tuple(sorted(s)) not in sorted_strs: #cast to tuple since list can't be key
                sorted_strs[tuple(sorted(s))] = [s] #tuples arent mutable, lists are
            else:
                sorted_strs[tuple(sorted(s))].append(s)
        return list(sorted_strs.values()) #returns view object, cast to list