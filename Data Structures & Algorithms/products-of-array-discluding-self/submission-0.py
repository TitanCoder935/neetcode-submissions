import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            mult=1
            for i2 in range(len(nums)):
                if(i2!=i):
                    mult*= nums[i2]
            res.append(mult)
        return res




        