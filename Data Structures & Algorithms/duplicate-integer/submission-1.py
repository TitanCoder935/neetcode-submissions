class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counting_list=[]
        for i in nums :
            if i not in counting_list:
                counting_list.append(i)
            else:
                return True

        return False
        