class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        i2=1
        while(i < len(nums)-1):
            if(nums[i]+nums[i2]==target):
                return [i,i2]
            elif(i2>=len(nums)-1):
                i+=1
                i2=i+1
            else:
                i2+=1

        
                




        