class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            count = [0] * 26 # count of each letter a-z
            for char in s:
                count[ord(char) - ord("a")] += 1
            if tuple(count) not in map:
                map[tuple(count)] = [s]
            else:
                map[tuple(count)].append(s)
        return list(map.values())