from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) == len(t):
#             if sorted(s) == sorted(t):
#                 return True
#         return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("racecar", "carrace"))
    print(solution.isAnagram("jar", "jam"))
