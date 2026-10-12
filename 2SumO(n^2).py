def sum2(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]
    return [-1,-1]
arr=list(map(int,input().split()))
target=int(input())
print(sum2(arr,target))