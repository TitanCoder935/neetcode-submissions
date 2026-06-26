class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for i2 in range(len(numbers)):
                if(i!=i2 and numbers[i] + numbers[i2]==target):
                    return [i+1, i2+1]
                else:
                    continue
            
        