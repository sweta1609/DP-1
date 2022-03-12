from sys import stdin
from sys import maxsize as MAX_VALUE
import sys



def countMinStepsToOne(n) :
    pass
    dp = [-1 for i in range(n+1)]
    dp[1] = 0
    dp[0] = 0
    for i in range(2 , n+1):
        
        if dp[i] == -1:
            ans1 = dp[i-1]
            
        if i%2 == 0:
            x = i//2
            if dp[i//2] == -1:
                ans2 = 1 + dp[x//2]
            else:
                ans2 = dp[i//2]
        else:
            ans2 = sys.maxsize
            
        if i%3 == 0:
            y = i//3
            if dp[i//3] == -1:
                ans2 = 1 + dp[y//3]
            else:
                ans3 = dp[i//3]
        else:
            ans3 = sys.maxsize
            
        ans = 1 + min(ans1,ans2,ans3)
        dp[i] = ans
    return dp[n]



#main
n = int(stdin.readline().rstrip())
print(countMinStepsToOne(n))
