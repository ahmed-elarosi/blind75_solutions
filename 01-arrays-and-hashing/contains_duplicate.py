from typing import List

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#             empty_list = []
#             for i in range(len(nums)):
#                   num = nums[i]
#                   if num not in empty_list:
#                         empty_list.append(num)
#             print(empty_list)
#             return empty_list != nums


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True

#         return False


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#   sorted_nums = sorted(nums)
#   for i in range(len(sorted_nums) - 1):
#       nxt = i + 1
#       if sorted_nums[i] == sorted_nums[nxt]:
#           return True
#   return False+


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         print(set(nums))
#         return len(set(nums)) < len(nums)


if __name__ == "__main__":

    solution = Solution()
    print(solution.hasDuplicate([1, 2, 3, 3]))
    print(solution.hasDuplicate([1, 2, 3, 4]))
    print(solution.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
