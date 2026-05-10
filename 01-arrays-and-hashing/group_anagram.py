from typing import List, DefaultDict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = DefaultDict(list)


if __name__ == "__main__":
    solution = Solution()
    strings = ["act", "pots", "tops", "cat", "stop", "hat"]
    strings_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strings))
    print(solution.groupAnagrams(strings_1))
