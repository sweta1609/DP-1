import sys,math
def minStepsTo1(n):
    #Implement Your Code Here
    pass
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(1,n+1):
        ans = sys.maxsize
        root = int(math.sqrt(i))
        for j in range(1,root+1):
            currAns = 1 + dp[i-(j*j)]
            ans = min(ans,currAns) #minimum of previous ans and current ans
        dp[i] = ans
    return dp[n]

        

    
n = int(input())
ans = minStepsTo1(n)
print(ans)

