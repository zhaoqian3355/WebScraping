class Solution:
    def lengthOfLongestSubstring(self,s):
        strList=[]
        for counter,option in enumerate(s):
            subS=s[counter+1:]
            for subCounter,subOption in enumerate(subS):
                if option==subOption:
                    strList.append(s[counter:counter+1+subCounter])
                    break
        
        maxLength=0
        for option in strList:
            optionLength=len(option)
            if optionLength>maxLength:
                maxLength=optionLength
        return strList


solution=Solution()

print(solution.lengthOfLongestSubstring("abcdeafghiasdfa"))

a=""
input(a)