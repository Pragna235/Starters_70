# cook your dish here
for t in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    cost=0
    
    for i in range(n):
        if(arr[i]>=x):
            cost+=brr[i]
            
    print(cost)
        