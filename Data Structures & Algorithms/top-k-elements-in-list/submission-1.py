import numpy as np

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for n in nums:
            if(n not in dic):
                dic[n]=1
            else:
                dic[n]+=1
        print(dic)
        freq=[]
        for key,v in dic.items():
            if(len(freq)<k):
                freq.append(v)
                print(freq)
            elif(min(freq)<v):
                x=freq.index(min(freq))
                freq[x]=v
                print(freq)
                
        f=[]
        for number, frequency in dic.items():
            if(frequency in freq):
                f.append(number)
        return f

            

        











