class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for i in range(len(numbers)):
    #         for i2 in range(len(numbers)):
    #             if(i!=i2 and numbers[i] + numbers[i2]==target):
    #                 return [i+1, i2+1]
    #             else:
    #                 continue
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            solution = numbers[left] + numbers[right]

            if solution == target:
                return [left + 1, right + 1]
            elif solution < target:
                left += 1
            else:
                right -= 1


    
            
        