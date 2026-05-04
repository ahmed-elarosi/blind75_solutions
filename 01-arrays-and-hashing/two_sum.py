from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for index1 in range(len(nums)):
#             for index2 in range(index1 +1, len(nums)):
#                 if nums [index1] + nums [index2] == target:
#                     return [index1, index2]
        
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i in range(len(nums)):
            num = nums[i]
            #print("num:",num)
            if target - num in seen:
                return [i, seen[target-num]]
            seen[num] = i
        return []
#seen{2:0, }



if __name__ == "__main__":
    solution = Solution()
    #print(solution.twoSum([4, 7, -1, 5], 4))
    print(solution.twoSum([2, 7, 11, 15], 9)) 