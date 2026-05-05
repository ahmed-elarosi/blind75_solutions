from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            empty_list = []
            for i in range(len(nums)):
                  num = nums[i]
                  if num not in empty_list:
                        empty_list.append(num)
            print(empty_list)     
            return empty_list != nums
                        
                  
                  


if __name__ == "__main__":
      solution = Solution()
      print(solution.hasDuplicate([1, 2, 3, 3]))
      print(solution.hasDuplicate([1, 2, 3, 4]))
      print(solution.hasDuplicate([1, 1, 1,3, 3, 4,3, 2, 4, 2]))