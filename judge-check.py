class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting =[0]*(n+1)
        trusted  =[0]*(n+1)
        
        for p1, p2 in trust:
            trusting[p1]-=1
            trusted[p2]+=1
        for i in range (1,n+1):
            if (trusting[i]==0 and trusted[i]==n-1):
                return i
        return -1
