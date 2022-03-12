def lisI(li, n):
    dp = [[0 for j in range(2)] for i in range(n+1)]
    
    for i in range(n-1,-1,-1):
        including_max = 1
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                including_max = max(including_max, 1+dp[j][0])
        dp[i][0] = including_max
        excluding_max = dp[i+1][1]
        overallMax = max(including_max, excluding_max)
        dp[i][1] = overallMax
        
    return dp[0][1]

n = int(input())
arr = list(int(ele) for ele in input().split())

print(lisI(arr, n)) 
