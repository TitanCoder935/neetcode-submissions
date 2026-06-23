class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        dic2={}
        i=0
        if(len(s)!= len(t)):
            return False
        else:
            while(i<len(s)):
                if s[i] not in dic:
                    dic[s[i]]=1
                else:
                    dic[s[i]]+=1
                if t[i] not in dic2:
                    dic2[t[i]]=1
                else:
                    dic2[t[i]]+=1
                i+=1
        
        if(dic==dic2):
            return True
        else:
            return False

        # if(len(s)!=len(t)):
        #     return False
        # else:
        #     for string in s:
        #         if(string not in t):
        #             return False
        #     return True




        