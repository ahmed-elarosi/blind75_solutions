from typing import List
from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            dic["".join(sorted(word))].append(word)
        return list(dic.values())


if __name__ == "__main__":
    solution = Solution()
    strings = ["act", "pots", "tops", "cat", "stop", "hat"]
    strings_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strings))
    print(solution.groupAnagrams(strings_1))
