class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each and store in a dictionary with sorted: [original]
        # so if next string(sorted) is in keys , attach to the values
        # iterate through the values and return result.

        visited = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            visited.setdefault(sort_s, []).append(s)
            # val = visited.get(sort_s, [])
            # val.append(s)
            # visited[sort_s] = val
        return list(visited.values())