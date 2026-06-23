class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            key= ''.join(sorted(word))
            if( key not in dic):
                dic[key]=[]
            dic[key].append(word)
        result=[]
        
        for k,v in dic.items():
            result.append(v)
        return result

        

            



                

        


        


        
        