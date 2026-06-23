class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup=[]
        for n in nums:
            if(n not in dup):
                dup.append(n)
            else:
                return True
        return False

            

        # dic={}
        # for i in range(len(nums)):
        #     if(nums[i] not in dic):
        #         dic.append(nums[i],1)
            
        